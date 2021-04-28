# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

import logging
logger = logging.getLogger(__name__)
import os, datetime, codecs, zipfile
from urllib.request import urlopen, urlretrieve
from noethysweb import version
from django.core.management import call_command
from django.conf import settings
from django.core.cache import cache


def Recherche_update():
    # Lecture de la version disponible en ligne
    fichier = urlopen("https://raw.githubusercontent.com/Noethys/Noethysweb/master/noethysweb/versions.txt", timeout=5)
    changelog = fichier.read().decode('utf-8')
    fichier.close()

    # Lecture du numéro de version online
    pos_debut_numVersion = changelog.find("n")
    pos_fin_numVersion = changelog.find("(")
    version_online_txt = changelog[pos_debut_numVersion + 1:pos_fin_numVersion].strip()
    version_online_tuple = version.GetVersionTuple(version_online_txt)
    logger.debug("version disponible =" + version_online_txt)

    # Lecture version actuelle
    version_actuelle_txt = version.GetVersion()
    version_actuelle_tuple = version.GetVersionTuple(version_actuelle_txt)
    logger.debug("version actuelle =" + version_actuelle_txt)

    # Comparaison des versions
    if version_online_tuple <= version_actuelle_tuple:
        logger.debug("Pas de nouvelle version disponible")
        return False, changelog

    return version_online_txt, changelog


def Update():
    # Recherche une version disponible
    version_online_txt, changelog = Recherche_update()
    if not version_online_txt:
        return False

    # Téléchargement du zip
    nom_fichier = "Noethysweb-%s.zip" % version_online_txt
    if not os.path.isdir(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)
    rep_temp = settings.MEDIA_ROOT + "/temp"
    if not os.path.isdir(rep_temp):
        os.mkdir(rep_temp)
    chemin_fichier = os.path.join(rep_temp, nom_fichier)
    try:
        logger.debug("Telechargement de la version %s..." % version_online_txt)
        url_telechargement = "https://github.com/Noethys/Noethysweb/archive/%s.zip" % version_online_txt
        urlretrieve(url_telechargement, chemin_fichier)
    except Exception as err:
        logger.debug("La nouvelle version '%s' n'a pas pu etre telechargee." % version_online_txt)
        logger.debug(err)
        return False

    # Dezippage
    logger.debug("Dezippage du zip...")
    zfile = zipfile.ZipFile(chemin_fichier, 'r')
    liste_fichiers = zfile.namelist()

    # Remplacement des fichiers
    prefixe = "Noethysweb-%s/noethysweb/" % version_online_txt
    chemin_dest = os.path.join(settings.BASE_DIR, "")

    logger.debug("Installation des nouveaux fichiers...")
    for i in liste_fichiers:
        d = i.replace(prefixe, "")
        if len(d) > 1 and not d.startswith("noethysweb-%s" % version_online_txt):
            if i.endswith('/'):
                try:
                    os.makedirs(os.path.join(chemin_dest, d))
                except:
                    pass
            else:
                try:
                    os.makedirs(os.path.join(chemin_dest, os.path.dirname(d)))
                except:
                    pass
                nom_fichier_temp = os.path.join(chemin_dest, d)
                if os.path.isdir(nom_fichier_temp):
                    os.rmdir(nom_fichier_temp)
                data = zfile.read(i)
                fp = open(nom_fichier_temp, "wb")
                fp.write(data)
                fp.close()

    zfile.close()
    os.remove(chemin_fichier)
    logger.debug("Installation terminee.")

    # Efface le numéro de version du cache
    cache.delete('version_application')

    # AutoReloadWSGI
    logger.debug("AutoReloadWSGI...")
    AutoReloadWSGI()

    # Collectstatic
    logger.debug("Collectstatic...")
    call_command('collectstatic', verbosity=0, interactive=False)

    # Mise à jour de la DB
    logger.debug("Migration DB...")
    #call_command('makemigrations')
    call_command('migrate')

    logger.debug("Mise a jour terminee.")
    return True


def AutoReloadWSGI():
    nom_fichier = os.path.join(settings.BASE_DIR, "noethysweb/wsgi.py")

    # Ouverture du fichier
    fichier_wsgi = open(nom_fichier, "r")
    liste_lignes_wsgi = fichier_wsgi.readlines()
    fichier_wsgi.close()

    # Modification du fichier
    fichier_wsgi = codecs.open(nom_fichier, 'w')
    for ligne in liste_lignes_wsgi:
        if "lastupdate" in ligne:
            ligne = "# lastupdate = %s" % datetime.datetime.now()
        fichier_wsgi.write(ligne)
    fichier_wsgi.close()


if __name__ == '__main__':
    Update()
