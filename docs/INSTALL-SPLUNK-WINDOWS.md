# Préparer Splunk Enterprise sous Windows

1. Vérifier Splunk Web sur `http://localhost:8000` et noter la version.
2. Dans **Settings → Forwarding and receiving → Configure receiving → New Receiving Port**, activer `9997`.
3. Si HEC est requis : **Settings → Data Inputs → HTTP Event Collector**, activer HEC et créer un token dédié au lab. Ne pas commiter le token.
4. Créer les index `win_event`, `linux`, `network`, `cloud`, `saas`, `security`, `lab_api` via **Settings → Indexes → New Index**.
5. Depuis Ubuntu, tester `nc -vz <IP_DU_PC> 9997`.
6. Confirmer les règles du pare-feu Windows et limiter les connexions au réseau de lab.

Le fichier `splunk/indexes.conf` est un modèle de référence ; l'UI est le chemin le plus simple pour un lab Windows mono-instance.
