from __future__ import annotations

from typing import List, Optional
from enum import Enum

from pydantic import BaseModel, Field
from api.utils import AutoIncrement


class FileExtention(str, Enum):
    """
    Enumération des extensions de fichiers.
    """
    TXT = "txt"
    JSON = "json"
    CSV = "csv"
    XML = "xml"
    HTML = "html"
    PDF = "pdf"
    DOCX = "docx"
    XLSX = "xlsx"
    PPTX = "pptx"
    JPG = "jpg"
    PNG = "png"
    MP4 = "mp4"
    AVI = "avi"
    MKV = "mkv"


class FolderBase(BaseModel):
    """
    Modèle de données de base pour les dossiers.

    :param id: ID du dossier
    :param name: Nom du dossier
    :param parent: Dossier parent
    """

    id: int = Field(..., title="ID du dossier", default_factory=AutoIncrement.next)
    name: str = Field(..., title="Nom du dossier")
    parent: FolderBase | None = Field(None, title="Dossier parent")


    def __init__(self, name:str, parent: FolderBase | None) -> None:
        """
        Constructeur de la classe FolderBase.

        :param name: Nom du dossier
        :param parent: Dossier parent
        """

        self.name = name
        if parent:
            try:
                parent.add_folder(self)
                self.parent = parent
            except Exception as e:
                raise e

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.name})"
    
    def add_file(self, file: FileBase) -> None:
        raise NotImplementedError
    
    def add_folder(self, folder: FolderBase) -> None:
        raise NotImplementedError
    
    def get_path(self) -> str:
        raise NotImplementedError
    

class FileBase(BaseModel):
    """
    Modèle de données de base pour les fichiers.

    :param id: ID du fichier
    :param name: Nom du fichier
    :param extension: Extension du fichier
    :param weight: Poids du fichier
    :param folder_id: ID du dossier parent
    :param folder: Dossier parent
    """

    id: int = Field(..., title="ID du fichier", default_factory=AutoIncrement.next)
    name: str = Field(..., title="Nom du fichier")
    extension: FileExtention = Field(..., title="Extension du fichier")
    weight: int = Field(..., title="Poids du fichier")
    folder: FolderBase = Field(..., title="Dossier parent")
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.name})"
    
    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.folder.add_file(self)