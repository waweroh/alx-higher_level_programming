#!/bin/bash
# display http methods accepted by server
curl -si -X "OPTIONS" $1 | grep "Allow" | cut -d " " -f 2-
