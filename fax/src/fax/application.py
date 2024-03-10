""" Variables globales de l'application. """

from __future__ import annotations

import os


# Nom de l'application
APPLICATION_NAME: str = "Fax"

# Chemin du répertoire courant
APPLICATION_DIR: str = os.path.dirname(os.path.realpath(__file__))

# Chemin du répertoire du projet
PROJECT_DIR: str = os.path.abspath(os.path.join(APPLICATION_DIR, *[os.pardir] * 3))

# Erreur d'appel invalide
INVALID_CALL_ERROR: str = "Cette méthode ne peut être appelée qu'une seule fois."


class ApplicationModuleError(Exception):
    """Erreur de module de l'application."""

    pass


class Module:
    """
    Représente un module de l'application.
    :param name: Nom du module.
    :param path: Chemin du module.
    """

    _name: str = ""
    _path: str = ""
    _fax: Module | None = None
    _api: Module | None = None
    _web_api: Module | None = None
    _mobile: Module | None = None
    _desktop: Module | None = None

    def __init__(self) -> None:
        """Constructeur du module."""
        pass

    def __str__(self) -> str:
        """Retourne une représentation du module."""

        return f"Module({self.name}, {self.path})"

    def __repr__(self) -> str:
        """Retourne une représentation du module."""

        return f"Module({self.name}, {self.path})"

    @property
    def name(self) -> str:
        """Retourne le nom du module."""

        return self._name

    @property
    def path(self) -> str:
        """Retourne le chemin du module."""

        return self._path

    def __create_module(self, name: str, directory_name: str) -> Module:
        """
        Crée un module.
        :param name: Nom du module.
        :param directory_name: Nom du répertoire du module.
        :return: Module créé.
        """

        if not self._name and not self._path:
            self._name = name
            self._path = os.path.join(PROJECT_DIR, directory_name)

            return self
        raise ApplicationModuleError(INVALID_CALL_ERROR)

    @property
    def fax(self) -> Module:
        """Retourne le module de l'application."""

        if not self._fax:
            self._fax = self.__create_module(APPLICATION_NAME, "fax")

        return self._fax

    @property
    def api(self) -> Module:
        """Retourne le module de l'API."""

        if not self._api:
            self._api = self.__create_module("API", "api")

        return self._api

    @property
    def web_api(self) -> Module:
        """Retourne le module de l'API Web."""

        if not self._web_api:
            self._web_api = self.__create_module("Web API", "web_api")

        return self._web_api

    @property
    def mobile(self) -> Module:
        """Retourne le module de l'application mobile."""

        if not self._mobile:
            self._mobile = self.__create_module("Mobile", "mobile")

        return self._mobile

    @property
    def desktop(self) -> Module:
        """Retourne le module de l'application de bureau."""

        if not self._desktop:
            self._desktop = self.__create_module("Desktop", "desktop")

        return self._desktop


# Liste des modules de l'application
FAX = Module().fax
API = Module().api
WEB_API = Module().web_api
MOBILE = Module().mobile
DESKTOP = Module().desktop
