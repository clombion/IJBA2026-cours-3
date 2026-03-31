---
name: data-stream-filter
description: Filter large datasets (CSV, JSON, ZIP) directly from a URL stream without downloading the entire file. Use when working with datasets that exceed local storage or when only a specific subset of data is needed.
---

# 🚀 Data Stream Filter

This skill provides a memory-efficient workflow for processing massive datasets (1GB+) on systems with limited disk space, such as cloud IDEs or CI/CD pipelines.

## 🛠️ Workflow

Follow these steps to extract only the data you need from a remote source:

### 1. URL Analysis
Identify the direct download URL for the dataset.
- Use `curl -L -I <URL>` to check headers (Content-Length, Content-Type).
- If the URL is for a page, use `web_fetch` or the API to find the raw file resource.

### 2. Schema Discovery
Fetch only the beginning of the file to understand its structure.
- **CSV**: `curl -s -L -r 0-2000 <URL> | head -n 1`
- **JSON**: `curl -s -L -r 0-5000 <URL> | head -c 5000`

Identify the column index (for CSV) or field path (for JSON) that will be used for filtering.

### 3. Stream Filtering (Execution)
Process the stream using pipes to avoid saving the full file to disk.

- **CSV with awk**:
  ```bash
  curl -s -L <URL> | awk -F ',' 'NR==1 || $INDEX ~ /PATTERN/ {print $0}' > filtered.csv
  ```
- **JSON with jq**:
  ```bash
  curl -s -L <URL> | jq -c '.[] | select(.field == "value")' > filtered.json
  ```
- **ZIP Extraction**:
  ```bash
  curl -s -L <URL> | funzip | awk ... # For single-file zips
  # OR for multi-file zips:
  curl -L <URL> -o temp.zip && unzip temp.zip "pattern*" && rm temp.zip
  ```

### 4. Validation
Verify the resulting file size and row count.
- `wc -l filtered.csv`
- `du -h filtered.csv`

## 📦 Resources

- **References**: `references/cheat_sheet.md` - Common patterns for awk, jq, and unzip.
- **Scripts**: `scripts/diagnose_remote.sh` - Automated tool to check remote file structure.
