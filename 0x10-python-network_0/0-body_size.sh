#!/bin/bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a HEAD request to the URL and display the size of the response body in bytes
curl -sI "$1" | grep -i '^Content-Length:' | awk '{print $2}'