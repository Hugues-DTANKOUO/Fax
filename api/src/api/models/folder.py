import datetime


class Folder:
    def __init__(self, folder_name):
        """
        Constructeur de la classe Folder.

        Args:
            name (str): Le nom du dossier.
        """
        self.folder_name = folder_name
        self.date_creation = datetime.datetime.now()  # Date de création du dossier
        self.date_modification = (
            datetime.datetime.now()
        )  # Date de modification du dossier
        self.file_list = []  # Liste des fichiers dans le dossier

    def add_file(self, file):
        """
        Ajoute un fichier au dossier.

        Args:
            file (File): Le fichier à ajouter.
        """
        self.file_list.append(file)
        self.date_modification = datetime.datetime.now()

    def remove_file(self, file):
        """
        Supprime un fichier du dossier.

        Args:
            file (File): Le fichier à supprimer.
        """

        # On vérifie si le fichier est dans le dossier
        if file in self.file_list:
            self.file_list.remove(file)
            self.date_modification = datetime.datetime.now()
        else:
            print("Le fichier n'existe pas dans le dossier.")

    def get_file_list(self):
        """
        Retourne la liste des fichiers dans le dossier.
        Les fichiers sont triés par ordre alphabétique.

        Returns:
            sorted_files: La liste des fichiers triés par ordre alphabétique.
        """
        return sorted(self.file_list)

    def get_folder_info(self):
        """
        Retourne les informations du dossier.

        Returns:
            dict: Les informations du dossier.
        """
        return {
            "folder_name": self.folder_name,
            "date_creation": self.date_creation,
            "date_modification": self.date_modification,
            "file_list": self.file_list,
        }
