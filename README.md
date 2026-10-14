# Splunk SOC Ingestion Lab v1.1
**Parcours pratique : architecture de collecte, parsing, TA/CIM et qualité des données**  
Durée : 40–60 h | Langue : français | Cible : Splunk Enterprise déjà installé sous Windows.

## Objectifs
1. Concevoir et déployer une collecte hybride : Universal Forwarder (UF), Syslog, collecteur, API/HEC.
2. Développer et maintenir parsing, timestamps, extractions et normalisation.
3. Créer un Technical Add-on (TA) versionné et mapper les champs vers CIM.
4. Contrôler qualité, exhaustivité, fraîcheur, duplication et dérive de format.

## Architecture cible
```text
PC Windows — Splunk Enterprise (10.50.0.10, exemple)
  Web 8000 | management 8089 | S2S receiving 9997 | HEC 8088
      ▲ UF/S2S                 ▲ HTTP Event Collector
      │                        │
VM Ubuntu (10.50.0.40, exemple)
  Syslog-ng OU rsyslog, générateurs, fichiers Linux, API simulée
      ▲
      └── Syslog UDP/TCP 5514 (port de lab non privilégié)

VM Windows optionnelle (10.50.0.50)
  Universal Forwarder, Windows Event Logs, Sysmon facultatif
```
Le plan IP est indicatif. Adaptez-le à votre réseau privé host-only/NAT. Ne publiez pas Splunk ni les ports de collecte sur Internet. Un Heavy Forwarder n'est pas requis au démarrage.

## Démarrage rapide
1. Lire `docs/ARCHITECTURE.md`, `docs/SECURITY.md`, `docs/INSTALL-SPLUNK-WINDOWS.md`.
2. Activer le receiving TCP 9997 dans Splunk Web.
3. Créer les index listés dans `splunk/indexes.conf` via Splunk Web ou une app locale.
4. Suivre `docs/INSTALL-UBUNTU.md`.
5. Configurer les fichiers `configs/uf-*` sur un UF, si installé.
6. Déployer `addons/TA-soc-firewall` sur le composant de parsing/search-time approprié.
7. Suivre `exercises/WORKBOOK.md`, puis comparer avec `instructor/ANSWER-KEY.md`.
8. Exécuter les tests de `tests/ACCEPTANCE.md`.

## Modules et durée
| Module | Travail | Durée |
|---|---|---:|
| M0 | Architecture, contrat d'intake et modèle de menace | 3 h |
| M1 | UF, S2S, inputs/outputs, index et sourcetype | 6 h |
| M2 | Syslog, collecteur, permissions, buffer et rotation | 7 h |
| M3 | API/HEC, pagination, retry, checkpoint et secrets | 6 h |
| M4 | Parsing, timestamps, event breaking, extractions | 8 h |
| M5 | TA, CIM, tests de non-régression, versioning | 8 h |
| M6 | Qualité, exhaustivité, fraîcheur, alertes | 7 h |
| M7 | Incidents, restitution et projet final | 5 h |

## Arborescence
`docs/` architecture/runbooks ; `configs/` UF ; `collectors/` Syslog/API ; `addons/` TA ; `datasets/` événements synthétiques ; `exercises/` travaux ; `tests/` acceptation ; `instructor/` corrigés ; `scripts/` validation.

## Limites
Les données cloud/SaaS sont synthétiques et ne sont pas des exports officiels de fournisseurs. Les binaires/licences Splunk, Windows et Sysmon ne sont pas inclus. Toute configuration est un modèle à tester avec votre version. Ne commitez jamais tokens, clés, mots de passe ou données réelles.
