# Ceci est le point d'entré principal du projet *`FAX`*

Le projet `Fax` est construite autour de plusieurs modules qui sont orchestrés de façon astutieuse à partir de ce point d'entré. 

## Modules

Le projet `Fax` dispose des modules suivants :

- [API](../api/README.md): Ensemble de fonctions réutilisable pour construire l'application sur une plateforme dédié.
- [FAX Web API](../web_api/README.md): L'API web de l'application
- [FAX Mobile](../mobile/README.md): Module qui gère les versions mobiles de l'application
- [FAX Desktop](../desktop/README.md): Module qui gère ls versions web de l'application

## Développement

- [Configuration de l'environnement et installation des dépendances](/fax/docs/python-3-poetry.md)
- [Analyse statique du code](/fax/docs/lint.md)
- [Tests](/fax/docs/tests.md)
- Valide tes modifications en local en exécutant la commande :
    ```shell
    poetry run check
    ```
