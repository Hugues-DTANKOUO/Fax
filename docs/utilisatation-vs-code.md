# Contribuer au projet *`FAX`* sur Github depuis VS Code

## Crée un compte sur Github et connecte toi

Biensur si ce n'est pas encore le cas

## Rends toi sur le dépôt Github du projet

Si tu lis ce fichier, tu y es probablement déjà. Sinon, il s'agit de se rendre à l'addresse https://github.com/Hugues-DTANKOUO/Fax.
Profite pour laisser une étoile à ce dépôt Git et pour t'abonner à mon compte accessible par ce lien https://github.com/Hugues-DTANKOUO.

## Crée une copie personnelle du dépôt (Fork)

Une fois [sur le dépôt](https://github.com/Hugues-DTANKOUO/Fax), clique sur le bouton `Fork`, puis sur `Create fork`.

Copie l'adresse de ton fork. Elle ressemblera surêment à ça : https://github.com/<ton_pseudo_git>/Fax

## Installe Github sur ta machine si c'est pas encore fait

Pour vérifier si tu as git dans ton invite commande, éxecute la commande :
```shell
git
```

## Clone ton fork

- Ouvre `VS Code` dans le dossier où tu souhaites travailler pour ce projet. 
- Ouvre ton `terminal` dans `VS Code`
- Exécute la commande (Remplace `<adresse_de_ton_fork>` par l'addresse que tu as copié)
```shell
git clone <addresse_de_ton_fork>
```

## Installe les extensions GitHub suivantes dans ton VS Code

- `GitHub`
- `GitHub Markdown Preview`

## Configure un romote upstream

Pour suivre les changements du dépôt original, ajoute le dépôt original comme un remote "upstream" en utilisant la commande :
```shell
git remote add upstream https:github.com/Hugues-DTANKOUO/Fax
```

## Crée une nouvelle branche

Avant de faire les modifications, crée une nouvelle branche avec la commande
```shell
git checkout -b nom_de_la_branche
```
Tu peux également le faire dans `VS Code` en cliquant tout en bas à gauche sur le nom de ta branche (qui sans doute actuellement `main`)

![capture d'écran de la position de la branche sur VS Code](/assets/Screenshot/main-branch-vs-code.png)

Puis clique sur `Créez une nouvelle branche ...`, donne un nom simple et sans espace à ta branche (`snake_case` recommandé avec `_` ou `-`), enfin crée là.

![capture d'écran pour créer une nouvelle branche](/assets/Screenshot/create-branch-vs-code.png)

## Apporte tes modifications

Avant de le faire, assure toi d'avoir installer les dépendances du projet [avec poetry par ce lien](/fax/docs/python-3-poetry.md)

Utilise VS Code pour modifier le code comme tu sais le faire ou comme on l'a fait dans les exercices précédent de notre formation sur Python. 

## Pousse tes changements sur ton fork en ligne (`Commit`)

Utilise la commande : 
```shell
git add
```
Pour ajouter tes changements. puis la commande 
```shell
git commit -m "Ton message de commit"
```
Pour `commit` tes modifications.

Tu peux également le faire dans `VS Code` comme ceci :
Dans la barre de menus à gauche, clique sur l'icone 

![Git branch dans VS Code](/assets/Screenshot/git-branch-vs-code.png) 

Puis entre ton message de `commit` et clique sur `Validation`.

## Pousse ta branche vers ton `fork` sur Github

Éxecute la commande 
```shell
git push origin nom_de_la_branche
```

## Ouvre une Pull Request (PR)

Sur GitHub, 
- Vas sur [le dépôt original](https://github.com/Hugues-DTANKOUO/Fax) et clique sur *`"New pull request"`*
- Sélectionne ta branche et suis les instructions pour créer la `PR`.