#!/bin/bash
# Sends request to server to display specific message
curl -sX PUT -L -F "user_id=98" -H "Origin: You got me!" 0.0.0.0:5000/catch_me
