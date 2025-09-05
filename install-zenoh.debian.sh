#!/usr/bin/env bash
echo "Installing zenoh, adapted from instructions at:"
echo -e "\t https://zenoh.io/docs/getting-started/installation/"

curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg

sudo /bin/cat << EOF > /etc/apt/sources.list.d/zenoh.sources
Types: deb
URIs: https://download.eclipse.org/zenoh/debian-repo/
Suites: /
Signed-By: /etc/apt/keyrings/zenoh-public-key.gpg
EOF

sudo apt update && sudo apt install --yes zenoh

zenohd --version
