#!/usr/bin/env python3
"""Ajoute des événements SSH synthétiques au fichier indiqué."""
import argparse, datetime, random
p=argparse.ArgumentParser()
p.add_argument("--output",default="datasets/generated-linux-auth.log")
p.add_argument("--count",type=int,default=20)
a=p.parse_args()
with open(a.output,"a",encoding="utf-8") as f:
    for i in range(a.count):
        ts=datetime.datetime.now().strftime("%b %d %H:%M:%S")
        user=random.choice(["alice","bob","svc-backup","root"])
        if random.random()<.25:
            line=f"lab-linux sshd[{2000+i}]: Failed password for {user} from 192.0.2.{random.randint(1,254)} port {random.randint(1024,65535)} ssh2"
        else:
            line=f"lab-linux sshd[{2000+i}]: Accepted publickey for {user} from 198.51.100.{random.randint(1,254)} port {random.randint(1024,65535)} ssh2"
        f.write(f"{ts} {line}\\n")
