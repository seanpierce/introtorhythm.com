#!/bin/bash

ssh-keyscan -H 167.71.118.223 >> ~/.ssh/known_hosts

openssl aes-256-cbc -K $encrypted_ae9e2abb8f12_key -iv $encrypted_ae9e2abb8f12_iv
  -in deploy_key.enc -out ./deploy_key -d

eval "$(ssh-agent -s)"
chmod 600 ./deploy_key
echo -e "Host $SERVER_IP_ADDRESS\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
ssh-add ./deploy_key
ssh -i ./deploy_key root@167.71.118.223 pwd
cd apps/introtorhythm.com/
git pull origin master

echo "--------------------"