#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
http_status=$(curl -so /dev/null $1 -w %{http_code})
if [ "$http_status" -eq 200 ]; then
    curl "$1"
fi
