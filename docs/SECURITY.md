# Sécurité
- Utiliser un réseau isolé, host-only ou VLAN privé.
- Ne pas exposer 8089/9997/8088 sur Internet.
- Créer un token HEC dédié ; le garder dans une variable d'environnement ou fichier ignoré par Git.
- Utiliser des données synthétiques et des IP réservées à la documentation.
- Restreindre les comptes de service au minimum nécessaire.
- Injecter les pannes uniquement dans les flux de test.
