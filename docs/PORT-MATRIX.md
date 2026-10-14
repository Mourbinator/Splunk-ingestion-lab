| Port | Protocole | Usage | Restriction |
|---:|---|---|---|
| 8000 | TCP | Splunk Web | poste/lab |
| 8089 | TCP | management Splunk | admin uniquement |
| 9997 | TCP | receiving UF/S2S | réseau privé |
| 8088 | TCP | HEC | réseau privé |
| 5514 | UDP/TCP | Syslog de lab | réseau privé |
| 6514 | TCP | Syslog TLS si configuré | réseau privé |

PowerShell :
```powershell
Get-NetTCPConnection -State Listen | Where-Object LocalPort -in 8000,8088,8089,9997
```
