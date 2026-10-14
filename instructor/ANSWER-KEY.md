# Corrigés formateur

## Diagnostic par couches
1. Source : événement généré ? compteur source ?
2. Transport : IP, DNS, port, TCP/UDP, TLS, route, firewall.
3. Collecteur : listener, queue, permissions, rotation, disque.
4. UF/input : chemin exact, droits, input activé, checkpoint.
5. Parsing : sourcetype, timestamp, event breaking, props/transforms sur le bon tier.
6. Indexation : index, droits, routing et quotas.
7. Modèle : champs CIM, eventtypes, tags.
8. Qualité : retard, pertes, doublons et dérive.

## Commandes utiles
Linux: `ss -lntup`, `nc -vz 10.50.0.10 9997`, `sudo tcpdump -ni any port 5514`, `sudo journalctl -u rsyslog`.
Splunk Windows:
```powershell
& "$env:SPLUNK_HOME\bin\splunk.exe" btool outputs list --debug
& "$env:SPLUNK_HOME\bin\splunk.exe" btool inputs list --debug
& "$env:SPLUNK_HOME\bin\splunk.exe" btool props list soc:firewall --debug
& "$env:SPLUNK_HOME\bin\splunk.exe" btool transforms list soc_firewall_kv --debug
```

## Mapping attendu
`src_ip→src`, `dest_ip→dest`, `src_port`, `dest_port`, `protocol→transport`, `vendor_product`. L'alias ne normalise pas les valeurs : normaliser explicitement les actions et documenter les valeurs acceptées. Vérifier tags/eventtypes contre le modèle de données et la version Splunk utilisée.

## Erreurs fréquentes
9997 non activé ; IP hôte non joignable ; TCP/UDP confondus ; index absent ; TA sur le mauvais tier ; timestamp sans timezone ; HEC token exposé ; absence de checkpoint/retry ; données synthétiques présentées comme réelles.
