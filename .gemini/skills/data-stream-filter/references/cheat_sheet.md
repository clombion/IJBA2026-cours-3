# 📝 Data Stream Filtering Cheat Sheet

## 📊 CSV Processing (awk)

| Task | Command |
| :--- | :--- |
| **Filter by Column** | `awk -F ',' '$3 == "Value"'` |
| **Regex Match** | `awk -F ';' '$5 ~ /33[0-9]{3}/'` |
| **Keep Header** | `awk -F ',' 'NR==1 || $1 ~ /match/'` |
| **Sum Column** | `awk -F ',' '{sum += $4} END {print sum}'` |
| **Select Columns** | `awk -F ',' '{print $1 "," $3}'` |

*Tip: Use `NR==1` to always include the header in your output.*

## 📄 JSON Processing (jq)

| Task | Command |
| :--- | :--- |
| **Select from Array** | `jq '.[] \| select(.id == "33")'` |
| **Extract Values** | `jq -r '.[] \| .name'` |
| **Nested Field** | `jq '.[] \| select(.address.city == "Bordeaux")'` |
| **Convert to CSV** | `jq -r '.[] \| [@csv]'` |

## 🗜️ ZIP / Compression (unzip, zcat)

| Task | Command |
| :--- | :--- |
| **List Remote Zip** | `curl -L <URL> -o t.zip && unzip -l t.zip && rm t.zip` |
| **Extract to Stdout** | `unzip -p archive.zip "file.csv"` |
| **Stream Gzip** | `curl -s <URL.gz> \| zcat \| awk ...` |
| **Stream Single Zip** | `curl -s <URL.zip> \| funzip \| head` |

## 🔍 Discovery Commands

| Task | Command |
| :--- | :--- |
| **Check Headers** | `curl -I <URL>` |
| **First 2KB** | `curl -s -r 0-2048 <URL>` |
| **Header + 5 rows** | `curl -s <URL> \| head -n 6` |
