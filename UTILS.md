# Utilitaire pratique pour faire des bonnes contributions

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