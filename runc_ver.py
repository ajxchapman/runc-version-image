#!/usr/bin/env python3

import os
import json
import subprocess

# runc version 1.1.4
# commit: v1.1.4-0-g5fd4c4d1
# spec: 1.0.2-dev
# go: go1.17.10
# libseccomp: 2.5.4
output = {}
try:
    for line in subprocess.check_output([f"/proc/{os.getppid()}/exe", "--version"]).splitlines():
        parts = line.decode().split(' ')
        output[parts[0].strip(":")] = parts[-1]
except:
    pass
else:
    output["__ignore"] = "[ PID ]"
    print(json.dumps(output))