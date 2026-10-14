# Incident drill 05-sourcetype
## Symptôme
Événements étiquetés syslog au lieu de soc:firewall.

## Mission
1. Recueillir les preuves avant modification.
2. Isoler la couche fautive.
3. Corriger une cause à la fois.
4. Démontrer le rétablissement.
5. Ajouter un test de non-régression.

## Piste formateur
Corriger l'assignation au point d'entrée et valider le tier de parsing.
