#!/bin/bash
set -e

dnf install -y docker
systemctl enable --now docker
usermod -aG docker ec2-user || true
mkdir -p /home/ec2-user/ml-app
