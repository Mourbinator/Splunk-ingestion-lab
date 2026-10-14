# Architecture de collecte

## Chemin des événements
```text
Fichiers Linux ── UF/S2S :9997 ──────────────────┐
Windows Event Logs ── UF/S2S :9997 ─────────────┤
Firewall ── Syslog :5514 ── collecteur ── fichier/HEC ─┤── Splunk
API SaaS ── poller avec checkpoint ── HEC :8088 ──────┘
```

### Rôles
- **UF** : suivi de fichiers et collecte Windows ; transfert S2S avec ACK.
- **Syslog-ng/rsyslog** : réception, tampon, permissions, rotation et routage Syslog.
- **HEC** : entrée HTTP pour applications et connecteurs API.
- **TA** : contrat de parsing, extractions, alias, eventtypes, tags, documentation et tests.
- **Splunk** : indexation, recherches de qualité et détection.

N'activez pas plusieurs collecteurs sur le même port. Ne collectez pas deux fois le même fichier avec UF et Fluent Bit. Ajoutez un Heavy Forwarder uniquement si une exigence réelle de routage, traitement ou connectivité le justifie.

## Index et sourcetypes proposés
| Index | Usage |
|---|---|
| `win_event` | Windows Security/System/Application |
| `linux` | Linux auth/syslog |
| `network` | Firewall, IDS |
| `cloud` | AWS/Azure/GCP |
| `saas` | M365 et SaaS |
| `security` | Sysmon / sécurité |
| `lab_api` | API et HEC de laboratoire |

Les sourcetypes proposés sont décrits dans `../splunk/sourcetypes.md`. Le sourcetype doit refléter le format et non seulement le nom du produit.
