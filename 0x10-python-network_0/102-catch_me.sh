#!/bin/bash
# Sends request to server to display specific message
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
