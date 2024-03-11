# Contribuer au projet *`Fax`*

Nous sommes ravis que vous envisagiez de contribuez à `Fax` ! Toutes les contributions sont les bienvenues : améliorations de code, corrections de bugs, documentation, suggestions, etc.

## Comment contribuer

### Signaler des bugs

Si vous trouvez un bug, veuillez l'ouvrir sous forme d'issue en utilisant le modèle de rapport de bug fourni. Assurez-vous de décrire le problème de manière détaillée, en incluant : 

- Les étapes pour reproduire le bug
- Le comportement attendu
- Le comportement observé
- Des captures d'écran si possible

### Suggérer des améliorations

Pour toute suggestion d'amélioration ou demande de fonctionnalité, ouvrez une issue avec une description détaillée de l'amélioration proposée. Expliquez pourquoi vous pensez que cette amélioration serait utile et comment elle devrait fonctionner.

## Pull Requests

Nous accueillons chaleuresement les pull requests. Voici quelques lignes directrices à suivre pour contribuer :

#### 1. *Forker le dépôt* et suivez les instructions pour configurer votre espace de travail sur [VS Code](/docs/utilisatation-vs-code.md)

#### 2. *Installez les dépendances* et assurez-vous que le projet fonctionne correctement sur votre système. [(poetry)](/fax/docs/python-3-poetry.md)

#### 3. *Suivez les conventions de code* du projet. Pour ce projet Python, nous suivons [PEP 8](https://peps.python.org/pep-0008/) ([Petit résumé de PEP 8](/docs/PEP8-resume-fr.md)), assurez-vous donc de l'avoir lu et de l'appliquer.

#### 4. *Écrivez des tests pour les nouvelles fonctionnalités ou correction de bugs lorsque cela est possible.

#### 5. *Documentez votre code*, en particulier les nouvelles fonctionnalités. Assurez-vous d'ajouter ou de mettre à jour les commentaires dans le code et la documentation du projet si nécessaire.

#### 6. *Exécutez les tests* existants pour vous assurer que vous n'avez pas introduit de régressions.

Dans le repertoire [/fax](/fax/), exécutez la commande :
```shell
poetry run check
```

#### 7. *Soumettez votre pull request* avec une description détaillé de vos modifications. Incluez le contexte de ce que vous avez fait et pourquoi.

### Processus de revue des Pull Requests

Chaque pull request sera examinée par les mainteneurs du projet. Nous pouvons demander des modifications ou apporter des suggestions avant de fusionner votre contribution. Nous visons à répondre aux PRs dans un délai de 2 jours maximum, mais selon le volume de contributions, cela peut varier.

## Code de conduite

En contribuant à ce projet, vous acceptez de respecter son code de conduite. Tout comportement inapproprié peut entraîner le retrait de votre contribution ou l'interdiction de participer.
Vous vous engagez également à ne jamais revendiquer la parternité partielle ou totale de ce projet. Vous avez le droit d'être citer parmis les contributeurs et d'utiliser ce projet dans le cadre décrit par sa licence.
