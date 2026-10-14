# Installation de la VM Ubuntu

- Ubuntu Server 22.04/24.04, 2 vCPU, 4–8 Go RAM, 30 Go disque.
- Installer les outils : `sudo apt update && sudo apt install -y git curl jq netcat-openbsd tcpdump python3 python3-venv`.
- Cloner le dépôt puis lire les configurations. Pour commencer, utiliser un seul démon Syslog (rsyslog ou syslog-ng).
- Le générateur utilise le port non privilégié 5514 : `python3 generators/send_syslog.py --host 127.0.0.1 --port 5514 --count 100`.
- Configurer l'UF seulement pour les fichiers locaux à collecter ; Syslog seul n'exige pas un UF.
- Pour HEC, définir `SPLUNK_HEC_URL` et `SPLUNK_HEC_TOKEN` dans l'environnement, sans les enregistrer dans Git.
