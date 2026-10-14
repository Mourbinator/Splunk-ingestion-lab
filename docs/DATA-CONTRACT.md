# Contrat d'intake : firewall synthétique

| Élément | Contrat |
|---|---|
| Sourcetype | `soc:firewall` |
| Index | `network` |
| Horodatage | `event_time` en ISO-8601 avec timezone |
| Champs requis | `event_id`, `src_ip`, `dest_ip`, `src_port`, `dest_port`, `action`, `protocol`, `rule_id` |
| Actions attendues | `allow`, `deny`, `drop` en brut ; valeurs normalisées documentées dans le TA |
| Fraîcheur cible | 95 % visibles en moins de 120 s dans le lab |
| Exhaustivité | comparer compteurs générateur, collecteur et Splunk sur la même fenêtre |
| Confidentialité | synthétique ; aucune donnée client |

Un intake est incomplet sans propriétaire, fréquence, volume, stratégie de retry, champs obligatoires, source de temps, index/sourcetype, tests, runbook et rollback.
