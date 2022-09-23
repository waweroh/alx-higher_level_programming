#!/bin/bash
# display json
curl -sX POST $1 -d @"$2" -H "Content-Type: application/json"
