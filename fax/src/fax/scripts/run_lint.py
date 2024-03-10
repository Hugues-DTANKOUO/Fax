""" Script d'exécution de Ruff, Black et MyPy sur l'ensemble des modules du projet. """

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

LINTERS = ["black", "mypy"]


def run() -> None:
    """Exécute Ruff, Black et Mypy sur l'ensemble des modules du projet."""

    # Exécution de Ruff, Black et Mypy sur l'ensemble des modules du projet
    print("Exécution de Ruff, Black et Mypy sur l'ensemble des modules du projet...")

    for module in MODULES:
        # Exécution de Ruff sur le module
        print(f"Exécution de Ruff sur le module {module.name}...")
        subprocess.run(["ruff", "check", module.path], check=True)

        for linter in LINTERS:
            print(f"Exécution de {linter} sur le module {module.name}...")
            subprocess.run([linter, module.path], check=True)
