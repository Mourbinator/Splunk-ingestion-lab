from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=["README.md","docs/ARCHITECTURE.md","docs/INSTALL-SPLUNK-WINDOWS.md","configs/uf-linux/outputs.conf","addons/TA-soc-firewall/default/props.conf","datasets/firewall.log","exercises/WORKBOOK.md","instructor/ANSWER-KEY.md","tests/ACCEPTANCE.md"]
missing=[p for p in required if not (root/p).exists()]
if missing: raise SystemExit("Missing files: "+", ".join(missing))
print(f"OK: {len(required)} required files present")
