# Utilitaire pratique pour faire des bonnes contributions

## Créer une branche pour écrire son code

## Pousser son code sur Github

## Récupérer le code de main sur sa branche en local

## Convertir un fichier `.ipynb` en fichier `.md`

Dans l'invite de commande, à la racine de ce projet, exécuter la commande :

```shell
pip install nbconvert
```
Si vous avez déjà installer `nbconvert`, se ne sera plus nécessaire les prochaines fois.

Exécutez ensuite la commande : 
```shell
jupyter nbconvert --to markdown TonNotebook.ipynb
```