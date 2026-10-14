#!/usr/bin/env python3
"""Messages Syslog synthétiques UDP/TCP. Défaut localhost:5514 UDP."""
import argparse, socket, time, random, datetime
p=argparse.ArgumentParser()
p.add_argument("--host", default="127.0.0.1")
p.add_argument("--port", type=int, default=5514)
p.add_argument("--count", type=int, default=10)
p.add_argument("--tcp", action="store_true")
a=p.parse_args()
typ=socket.SOCK_STREAM if a.tcp else socket.SOCK_DGRAM
with socket.socket(socket.AF_INET, typ) as s:
    if a.tcp: s.connect((a.host,a.port))
    for i in range(a.count):
        ts=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
        msg=(f"<134>1 {ts} firewall01 soc-firewall - - event_id=fw-{int(time.time())}-{i} "
             f"event_time={ts} src_ip=192.0.2.{random.randint(1,254)} "
             f"dest_ip=198.51.100.{random.randint(1,254)} src_port={random.randint(1024,65535)} "
             f"dest_port={random.choice([22,53,80,443,3389])} action={random.choice(['allow','deny','drop'])} "
             f"protocol={random.choice(['tcp','udp'])} rule_id=LAB-{random.randint(1,20)}")
        if a.tcp: s.sendall(msg.encode()+b"\\n")
        else: s.sendto(msg.encode(),(a.host,a.port))
        time.sleep(.05)
