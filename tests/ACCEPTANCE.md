# Tests d'acceptation

- [ ] Splunk Web accessible.
- [ ] 9997 écoute et est joignable depuis Ubuntu.
- [ ] HEC activé si utilisé, token non versionné.
- [ ] 100 événements générés et compteur source conservé.
- [ ] Sources ont index/sourcetype attendus.
- [ ] Pas de doublons évidents après redémarrage.

```spl
| tstats count where index=* by index sourcetype host
```
```spl
index=network sourcetype=soc:firewall
| stats count values(action) as actions values(protocol) as protocols
```
```spl
index=network sourcetype=soc:firewall
| eval missing=if(isnull(src_ip) OR isnull(dest_ip) OR isnull(action),1,0)
| stats count sum(missing) as missing max(_indextime) as last_index
```
Comparer les compteurs source/collecteur/Splunk sur la même fenêtre.
