#!/usr/sh

systemctl daemon-reload
systemctl start autodeploy
systemctl enable autodeploy