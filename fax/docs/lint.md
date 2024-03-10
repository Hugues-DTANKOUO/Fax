# Utilisation de `mypy`, `black` et `ruff` avec poetry dans le projet

Ce fichier contient des informations sur l'utilisation de mypy, black et ruff avec poetry dans le projet.

## mypy

[*`mypy`*](https://mypy.readthedocs.io/) est un outil de typage statique pour Python. Il permet de détecter les erreurs de typage avant l'exécution du code.

## black

[*`black`*](https://black.readthedocs.io/) est un outil de formatage de code pour Python. Il permet d'appliquer des règles de style cohérentes au code source, en le reformatant de manière automatique.

## ruff

[*`ruff`*](https://github.com/jwkvam/ruff) est un outil de linting pour Python. Il permet de détecter les erreurs de style, les problèmes de qualité de code et les violations des conventions de codage.

## Analyse Statique du code

Pour effectuer une analyse statique de ton code avec ces trois modules dans ce projet, exécute la commande `poetry` suivante dans le repertoire principal du projet :

```shell
poetry run lint
```