from datetime import datetime

from api.models.folder import Folder


def test_creation_dossier():
    """
    ÉTANT DONNÉ une représentation d'un dossier
    QUAND le dossier est créé
    ALORS le dossier possède les propriétés correctes et une liste de fichiers vide
    """
    folder_name = "MonDossierTest"
    folder = Folder(folder_name)

    assert folder.folder_name == folder_name
    assert isinstance(folder.date_creation, datetime)
    assert isinstance(folder.date_modification, datetime)
    assert len(folder.file_list) == 0


def test_ajout_fichier_dans_dossier():
    """
    ÉTANT DONNÉ une représentation d'un dossier
    QUAND un fichier est ajouté dans le dossier
    ALORS le fichier se trouve dans la liste de fichiers du dossier
    """
    folder_name = "MonDossierTest"
    folder = Folder(folder_name)
    file1 = "fichier1.txt"

    folder.add_file(file1)
    assert file1 in folder.file_list


def test_suppression_fichier_du_dossier():
    """
    ÉTANT DONNÉ une représentation d'un dossier avec un fichier
    QUAND le fichier est supprimé du dossier
    ALORS le fichier ne se trouve pas dans la liste de fichiers du dossier
    """
    folder_name = "MonDossierTest"
    folder = Folder(folder_name)
    file1 = "fichier1.txt"

    folder.add_file(file1)
    folder.remove_file(file1)
    assert file1 not in folder.file_list


def test_liste_fichiers_dossier():
    """
    ÉTANT DONNÉ une représentation d'un dossier avec des fichiers
    QUAND on demande la liste des fichiers du dossier
    ALORS les fichiers sont retournés triés par ordre alphabétique
    """
    folder_name = "MonDossierTest"
    folder = Folder(folder_name)
    file1 = "fichier1.txt"
    file2 = "fichier2.txt"

    folder.add_file(file2)
    folder.add_file(file1)
    assert folder.get_file_list() == [file1, file2]


def test_get_folder_info():
    """
    ÉTANT DONNÉ une représentation d'un dossier
    QUAND on demande les informations du dossier
    ALORS les informations du dossier sont retournées
    """
    folder_name = "MonDossierTest"
    folder = Folder(folder_name)

    expected_info = {
        "folder_name": folder_name,
        "date_creation": folder.date_creation,
        "date_modification": folder.date_modification,
        "file_list": folder.file_list,
    }

    assert folder.get_folder_info() == expected_info
