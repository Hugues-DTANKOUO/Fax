# CapWords & CamelCase

CapWords et CamelCase sont deux conventions de nommage utilisées en programmation pour nommer des éléments comme les classes, les méthodes, les variables, etc. Elles aident à rendre les noms plus lisibles en indiquant les limites des mots sans utiliser d'espaces. Voici une explication de chacune :

## CapWords

Aussi connue sous le nom de *PascalCase*, cette convention commence chaque mot par une majuscule et les joint sans espace. Elle est fréquement utilisée pour nommer les classes dans de nombreux langages de programmation, y compris Python. Par exemple, `NomDeClasse` est un identifiant écrit en CapWords. [PEP 8](PEP8-resume-fr.md) recommande d'utiliser `CapWords` pour nommer les classes en Python. Nous suivrons cette convention dans ce projet.

## CamelCase

`CamelCase` est similaire à `CapWords`, mais la différence réside dans la lettre initiale du premier mot : en `CamelCase`, la première lettre est en minuscule tandis qu'en `CapWords`, elle est en majuscule. `CamelCase` est souvent utilisé pour nommer des méthodes ou des variables dans certains langages de programmation. Par exemple, `nomDeVariable` ou `methodeDeCalcul` sont des identifiants écrits en `CamelCase`. Cependant, en Python, la convention [PEP 8](PEP8-resume-fr.md) recommande d'utiliser le `snake_case` (`nom_de_variable`, `methode_de_calcul`) pour les fonctions, méthodes, et variables plutôt que `CamelCase`.


##

En résumé, `CapWords` (ou `PascalCase`) commence chaque mot par une majuscule et est utilisée pour les noms de classes en Python, conformément à [PEP 8](PEP8-resume-fr.md). CamelCase commence le premier mot par une minuscule et est moins fréquement utilisé en Python pour les noms de fonctions et de variables, [PEP 8](PEP8-resume-fr.md) recommande plutôt l'utilisation de `snake_case` pour ces éléments.