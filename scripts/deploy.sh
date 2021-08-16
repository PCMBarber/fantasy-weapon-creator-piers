#!/bin/bash

rsync docker-compose.yaml nginx.conf swarm-manager:

ssh swarm-manager << EOF
export DATABASE_URI=$DATABASE_URI && docker stack deploy --compose-file docker-compose.yaml fantasy-weapon-generator
EOF