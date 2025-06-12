#!/usr/bin/env bash
# This script is used to submit the json file to the test server.
# Usage: ./run_test.sh <json_file>
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <json_file>"
    exit 1
fi
JSON_FILE=$1

SERVER_URL=${SERVER_URL:-"http://localhost:18000/predict"}

curl -X POST "$SERVER_URL" \
     -H "Content-Type: application/json" \
     -d "@$JSON_FILE" \
     -o response.json
if [ $? -ne 0 ]; then
    echo "Error: Failed to submit the request."
    exit 1
fi
echo "Response saved to response.json"