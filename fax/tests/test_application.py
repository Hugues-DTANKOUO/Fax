import os
from fax.application import (
    Module,
    APPLICATION_NAME,
    PROJECT_DIR,
    ApplicationModuleError,
    INVALID_CALL_ERROR,
    FAX,
    API,
    WEB_API,
    MOBILE,
    DESKTOP,
)


def test_globals_variables() -> None:
    """
    ÉTANT DONNÉ le projet fax.
    QUAND le projet est initialisé
    ALORS les variables globales sont correctement initialisées.
    """

    # Variables globales
    assert APPLICATION_NAME == "Fax"
    assert PROJECT_DIR == os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # Modules
    assert FAX.name == "Fax"
    assert FAX.path == os.path.join(PROJECT_DIR, "fax")

    assert API.name == "API"
    assert API.path == os.path.join(PROJECT_DIR, "api")

    assert WEB_API.name == "Web API"
    assert WEB_API.path == os.path.join(PROJECT_DIR, "web_api")

    assert MOBILE.name == "Mobile"
    assert MOBILE.path == os.path.join(PROJECT_DIR, "mobile")

    assert DESKTOP.name == "Desktop"
    assert DESKTOP.path == os.path.join(PROJECT_DIR, "desktop")


def test_invalid_module_creation() -> None:
    """
    ÉTANT DONNÉ un module du projet fax.
    QUAND on essaye de créer un autre module avec une propriété de ce dernier
    ALORS une erreur est levée.
    """

    # Tentative de création multiple d'un module
    module = Module().fax
    try:
        module.desktop
    except ApplicationModuleError as error:
        assert str(error) == INVALID_CALL_ERROR
    else:
        assert False
