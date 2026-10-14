# TA-soc-firewall v1.1
TA pédagogique pour contrat de données, parsing, alias CIM, eventtypes, tags et tests.

Copier le dossier dans `$SPLUNK_HOME/etc/apps/` sur le composant approprié, puis valider avec `btool`. Ne pas confondre parsing index-time et search-time. Adapter `default/` et `local/` selon le modèle de déploiement. Tester guillemets, champs absents, IPv6, valeurs échappées, timezone et évolutions du format avant production.
