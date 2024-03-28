#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
#curl -s -w "%{size_download}" "$1"
curl -so /dev/null "$1" -w '%{size_download}'; echo ""
