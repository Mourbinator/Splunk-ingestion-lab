# Cahier d'exercices v1.1

## E0 — Concevoir un intake (3 h)
Produire diagramme, contrat de données, index/sourcetype, champs requis, volumes, fréquence, SLO, sécurité, propriétaire, tests et rollback.

## E1 — UF/S2S (6 h)
Activer 9997, configurer `outputs.conf`, suivre un fichier, vérifier la connectivité et les événements. Injecter une mauvaise IP/port puis diagnostiquer sans réinstaller.
Validation : événements visibles dans le bon index et preuve conservée.

## E2 — Syslog/collecteur (7 h)
Lancer syslog-ng sur 5514/UDP ; générer 100 événements ; comparer compte généré/reçu/indexé. Tester TCP séparément. Simuler permissions incorrectes, rotation et indisponibilité de Splunk.
Questions : où une perte peut-elle survenir ? quelles preuves distinguent transport et indexation ?

## E3 — API/HEC (6 h)
À partir de `datasets/saas-audit.jsonl`, écrire ou spécifier un poller avec pagination, checkpoint, retry, 429, idempotence, métriques et secret externalisé. Livrer tests et runbook.

## E4 — Parsing/timestamps (8 h)
Ingest `datasets/firewall.log` en `soc:firewall`. Vérifier champs, timestamps et event breaking. Ajouter tests : champ absent, valeur citée, action inconnue, timezone invalide et format modifié.
```spl
index=network sourcetype=soc:firewall
| table _time event_id src_ip dest_ip src_port dest_port action protocol rule_id
```

## E5 — TA et CIM (8 h)
Lire `addons/TA-soc-firewall`; mapper `src_ip→src`, `dest_ip→dest`, `protocol→transport`, vérifier `src_port`, `dest_port`, `action`, `vendor_product`. Ajouter eventtypes/tags, tests et changelog. Documenter `default`/`local`, dépendances et rollback.

## E6 — Qualité (7 h)
Construire des contrôles de volume, retard, champs obligatoires, valeurs inconnues, doublons, dernière observation, erreurs HEC et dérive du format.
```spl
index=network sourcetype=soc:firewall earliest=-15m
| eval missing=if(isnull(src_ip) OR isnull(dest_ip) OR isnull(action),1,0)
| stats count sum(missing) as bad_events max(_indextime) as last_index by host
```
Comparer `_indextime` à un timestamp source fiable ; une horloge décalée fausse la mesure.

## E7 — Incident drill (5 h)
Choisir trois pannes de `exercises/incidents/`, recueillir les preuves, corriger une seule couche, démontrer le rétablissement et écrire le post-mortem.

## Projet final
Intégrer une nouvelle source. Livrer architecture, contrat, TA, tests de non-régression, recherches de qualité, runbook, rollback et démo de 10 minutes.
