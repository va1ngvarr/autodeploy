import os

service = f"""
[Unit]
Description=autodeploy
After=syslog.target
After=network.target

[Service]
WorkingDirectory={os.getcwd()}
ExecStart=/usr/bin/python3 autodeploy.py

[Install]
WantedBy=multi-user.target
"""

with open("/etc/systemd/system/autodeploy.service", "w") as f:
    f.write(service)

os.system("sh ./autodeploy-systemd.sh")
