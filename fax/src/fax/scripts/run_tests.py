""" Scripts d'exécution des tests unitaires sur l'ensemble des modules du projet. """

import subprocess

from fax.application import (
    FAX,
    API,
    WEB_API,
    MOBILE,
    DESKTOP,
    Module,
)

MODULES: list[Module] = [FAX, API, WEB_API, MOBILE, DESKTOP]


def run() -> None:
    """Exécute les tests unitaires sur l'ensemble des modules du projet."""

    print("Exécution des tests unitaires sur l'ensemble des modules du projet...")

    for module in MODULES:
        print(f"Exécution des tests unitaires sur le module {module.name}...")
        subprocess.run(["pytest", module.path, "-v"])
