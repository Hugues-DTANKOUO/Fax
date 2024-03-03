# Bon à savoir sur *`PEP 8`*

`PEP 8`, ou *"Python Enhancement Proposal 8"*, est un guide de style pour la rédaction de code Python qui établit une série de conventions visant à rendre le code Python clair, cohérent et facile à lire. Adopté par la communauté Python depuis sa création en 2001 par *Guido van Rossum*, *Barry Warsaw*, et *Nick Coghlan*, `PEP 8` joue un rôle crucial dans le maintien de l'uniformité et de la lisibilité du code au sein de vastes projets et entre différents projets Python. Voici un résumé détaillé des principales recommandations de `PEP 8`:

## Identation

Utilisez 4 espaces par niveau d'indentation pour distinguer clairement les blocs de code et respecter la structure hiérarchique du code.

## Longueur des lignes

Limitez les lignes de code à 79 caractères et les commentaires ou docstrings à 72 caractères pour améliorer la lisibilité sur différents dispositifs et éditeurs.

## Importation

Les importations doivent être placées en haut du fichier, juste après les commentaires du module et de la documentation du docstring, et avant les variables du module et les constantes globales.
Les importations doivent être groupées en trois catégories : bibliothèques standard, bibliothèques tierces, et modules locaux, chacune séparée par une ligne vide.

## Espaces

Les espaces sont préférés autour des opérateurs et après les virgules pour améliorer la lisibilité, mais évitez d'insérer des espaces immédiatement à l'intérieur des parenthèses, des crochets ou des accolades.

## Nommage

Les conventions de nommages dans `PEP 8` facilitent la distinction entre les différents types d'identifiants : 

- *Modules* : Utilisez des noms courts en minuscules, avec des underscores si nécessaire pour améliorer la lisibilité.

- *Classes* : Appliquez la convention [`CapWords` (ou `CamelCase`)](CapWords-CamelCase.md) pour nommer les classes.

- *Fonctions et variables* : Préférez les noms en minuscules avec des mots séparés par des underscores (`snake_case`) pour ces identifiants.

- *Constantes* : Écrivez les noms de constantes en majuscules avec des underscores séparant les mots.

## Expressions et Instructions

Les espaces doivent être utilisés de manière judicieuse dans les expresions et instructions pour distinguer les différents composants, comme après les virgules et autour des opérateurs d'assignation et de comparaison, mais évitez les espaces superflus à l'intérieur des parenthèses, crochets, et accolades.

## Commentaires

Les commentaires doivent être utilisés pour clarifier le code, notamment pour expliquer les décisions de conception, les algorithmes, et les complexités du code. Les commentaires doivent être à jour avec le code.

## Conclusion

`PEP 8` est conçu pour améliorer la maintenance et la compréhension du code Python, en promouvant un style de codage qui soit non seulement efficace mais aussi esthétiquement agréable. Suivre `PEP 8` n'est pas obligatoire mais fortement recommandé, surtout dans des environnements collaboratifs où la clarté et la cohérence du code sont essentielles pour le travail d'équipe et la maintenance du code à long terme.