""" Analyse statique du code et exécution des tests unitaires sur l'ensemble des modules du projet. """

from fax.scripts import run_lint, run_tests


def run() -> None:
    """Exécute l'analyse statique du code et les tests unitaires sur l'ensemble des modules du projet."""
    run_lint.run()
    run_tests.run()
