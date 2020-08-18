#!/bin/bash
# Curl a JSON file with POST request
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")
