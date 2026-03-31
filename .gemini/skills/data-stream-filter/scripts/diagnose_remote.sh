#!/bin/bash

# Simple script to diagnose a remote file for streaming
# Usage: ./diagnose_remote.sh <URL>

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

echo "--- 🔍 Remote File Diagnosis ---"
echo "URL: $URL"

# Check headers
echo -e "\n--- 📄 Headers ---"
curl -s -L -I "$URL" | grep -E "Content-Length|Content-Type|Last-Modified"

# Determine type and show preview
TYPE=$(curl -s -L -I "$URL" | grep -i "Content-Type" | awk '{print $2}' | tr -d '\r')

echo -e "\n--- 👁️ Preview (First 2KB) ---"
curl -s -L -r 0-2048 "$URL" | head -n 5

if [[ "$TYPE" == *"zip"* ]]; then
    echo -e "\n--- 🗜️ Archive Content (Listing) ---"
    curl -s -L "$URL" -o temp_diag.zip && unzip -l temp_diag.zip && rm temp_diag.diag
fi

echo -e "\n--- ✅ Done ---"
