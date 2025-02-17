# Redin 🕵️‍♂️

Redin is a powerful URL analyzer inspired by Raymond Reddington. Designed for bug bounty hunters and security researchers, Redin helps you discover interesting URLs, endpoints, and potential vulnerabilities by leveraging the OTX AlienVault API.

---

## Features ✨

- **URL Analysis**: Discover URLs associated with a domain or subdomain.
- **File Extension Filtering**: Automatically detect URLs with sensitive file extensions (e.g., `.conf`, `.sql`, `.bak`).
- **Keyword Filtering**: Identify URLs containing specific keywords (e.g., `admin`, `dashboard`, `redirect=`).
- **Pagination Support**: Fetch results from multiple pages of the OTX API.
- **Stylish Banner**: A visually appealing banner with Reddington's iconic quote.
- **Colorful Output**: Easy-to-read, color-coded results in the terminal.

---

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Redin.git
   cd Redin
   pip install requests pyfiglet colorama

## Usage 🚀

1. Prepare a `domains.txt` file with the domains/subdomains you want to analyze (one per line)
2. python3 redin.py domains.txt

## Configuration ⚙️

### File Extensions
You can customize the list of file extensions to search for by editing the `EXTENSIONS` list in the script:
```python
EXTENSIONS = [
    ".conf", ".bak", ".ini", ".tmp", ".zip", ".rar", ".7z", ".tar.xz", ".tar.bz2", ".tar.lz", ".zst", ".gzip",
    ".sql", ".db3", ".accde", ".accdt", ".ldb", ".ldf", ".dmp", ".rdb", ".json", ".pkl", ".feather", ".parquet",
    ".hdf5", ".mat", ".sas7bdat", ".xpt", ".dta", ".sav", ".rda", ".rdata", ".sqlite3", ".db-wal", ".db-shm",
    ".sqlitedb", ".ost", ".pst", ".edb", ".ns2", ".ns3", ".box", ".idx", ".eml", ".mbox", ".mail", ".msg", ".ics", ".vcf",
    ".backup", ".asp", ".aspx", ".jsp", ".pdf", ".csv", ".cgi"
]
```

## Example Output 📋
![image](https://github.com/user-attachments/assets/668700fd-a116-44dc-a253-81bb7e2e6574)

