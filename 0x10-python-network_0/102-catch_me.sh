#!/bin/bash
# sends request to server to display specific message
curl -sX PUT 0.0.0.0:5000/catch_me -L -F 'user_id=98' -H "Origin: You got me!"
