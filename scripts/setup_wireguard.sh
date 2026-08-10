#!/bin/bash
# Installs and configures WireGuard for secure database replication

apt-get update && apt-get install -y wireguard

# Generate keys
wg genkey | tee /etc/wireguard/privatekey | wg pubkey > /etc/wireguard/publickey

cat <<EOF > /etc/wireguard/wg0.conf
[Interface]
Address = 10.0.0.1/24
SaveConfig = true
ListenPort = 51820
PrivateKey = $(cat /etc/wireguard/privatekey)

[Peer]
PublicKey = <CLIENT_PUBLIC_KEY>
AllowedIPs = 10.0.0.2/32
EOF

systemctl enable wg-quick@wg0
systemctl start wg-quick@wg0
echo "WireGuard interface wg0 initialized."
