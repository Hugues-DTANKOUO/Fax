# Installation et utilisation de Poetry dans ce projet

## Installation de Poetry

Je t'invite à te reférer à [la documentation officielle](https://python-poetry.org/docs/)

Dans le cas contraire, voici un petit guide :

### Assure toi d'avoir `python 3.11` sur ta machine 
- Exécute la commande 
```shell
python --version
```
- Ou sous Linux et sur Mac, la commande
```shell
python3 --version
```
### Installe `pipx` [(documentation officielle)](https://pipx.pypa.io/stable/installation/)

- Exécute la commande suivante (sous Linux ou Mac, remplace `python` par `python3`)
```shell
python -m pip install pipx
```
- Vérifie que le chemin vers le scripts Python est ajouté à ta variable d'environnement PATH comme suit : 
```shell
python -m pipx ensurepath
```
- Redémarre ton terminal

- Vérifie que l'installation de `pipx` s'est faite correctement avec la commande :
```shell
pipx --version
```

### Installe `Poetry`
- À l'aide de `pipx`, exécute la commande
```shell
pipx install poetry
```

## Navigue vers le dossier principal du projet

Si tu te trouves déjà dans le dossier du grand projet, exécute la commande 
```shell
cd fax
```

## Installe les dépendances du projet

Une fois dans le dossier du projet, utilise `poetry` pour installer toutes les dépendances spécifiées dans le fichier [`pyproject.toml`](/fax/pyproject.toml):
```shell
poetry install
```
Cette commande crée un environnement virtuel pour le projet (s'il n'en existe pas déjà un) et installe toutes les dépendances nécessaires.

## Active l'environnement virtuel

Pour activer l'environnement virtuel géré par `poetry`, utilise la commande : 
```shell
poetry shell
```
Cette commande lance un nouveau shell où l'environnement virtuel est activé, vous permettant d'exécuter des commandes et des scripts dans le contexte de cet environnement. 

## Ajout de dépendances au projet

Vous n'aurez sans doute pas besoin de le faire.
Mai en cas de besoin, où vous avez l'habitude de faire 
```shell
pip install nom_de_la_dependance
```
Pour rajouter une dépendance à ce projet, vous devrez faire : 
```shell
poetry add nom_de_la_dependance
```