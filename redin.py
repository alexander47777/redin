import requests
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Function to display the banner
def display_banner():
    # Generate ASCII art for the tool name with a built-in font
    banner = pyfiglet.figlet_format("Redin", font="slant")  # Use a built-in font like "slant"
    
    # Add a tagline or description with emojis
    tagline = "💬 \"I’m a sin eater. I absorb the misdeeds of others,\n    darkening my soul to keep theirs pure. That is what\n    I’m paid for.\" - Raymond Reddington 💬"
    inspired_by = "🎬 Inspired by Raymond Reddington 🎬"
    author = "👨‍💻 __brave 👨‍💻"
    
    # Create a gradient effect for the banner text
    gradient_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    gradient_banner = ""
    for i, line in enumerate(banner.split("\n")):
        gradient_banner += gradient_colors[i % len(gradient_colors)] + line + "\n"
    
    # Print the banner with gradient colors and emojis
    print(gradient_banner)
    print(Fore.YELLOW + "╭" + "─" * 58 + "╮")
    print(Fore.GREEN + "│ " + tagline.center(56) + " │")
    print(Fore.MAGENTA + "│ " + inspired_by.center(56) + " │")
    print(Fore.YELLOW + "╰" + "─" * 58 + "╯")
    print(Fore.RED + "👨‍💻 __brave 👨‍💻")
    print(Fore.YELLOW + "╰" + "─" * 58 + "╯")
    print(Fore.YELLOW + "╰" + "─" * 58 + "╯")

# List of file extensions to search for
EXTENSIONS = [
    ".conf", ".bak", ".ini", ".tmp", ".zip", ".rar", ".7z", ".tar.xz", ".tar.bz2", ".tar.lz", ".zst", ".gzip",
    ".sql", ".db3", ".accde", ".accdt", ".ldb", ".ldf", ".dmp", ".rdb", ".json", ".pkl", ".feather", ".parquet",
    ".hdf5", ".mat", ".sas7bdat", ".xpt", ".dta", ".sav", ".rda", ".rdata", ".sqlite3", ".db-wal", ".db-shm",
    ".sqlitedb", ".ost", ".pst", ".edb", ".ns2", ".ns3", ".box", ".idx", ".eml", ".mbox", ".mail", ".msg", ".ics", ".vcf",
    ".backup", ".asp", ".aspx", ".jsp", ".pdf", ".csv", ".cgi"
]

# List of keywords to search for in URLs
KEYWORDS = [
    "internal", "admin", "return_url=", "redirect=", "dashboard", "report", "/api/", "url=", "finalURL=", "filename="
]

def fetch_and_extract_data(domain, max_pages=5):
    filtered_results = []
    
    for page in range(1, max_pages + 1):
        # Construct the API URL for the current page
        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/url_list?limit=500&page={page}"
        
        try:
            # Send a GET request to the API
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            
            # Parse the JSON response
            data = response.json()
            
            # Extract the 'url_list' from the response
            url_list = data.get("url_list", [])
            
            # If no more results are found, stop pagination
            if not url_list:
                print(f"{Fore.YELLOW}No more results found on page {page} for domain {domain}. Stopping pagination.{Style.RESET_ALL}")
                break
            
            # Filter URLs based on extensions and keywords
            for item in url_list:
                url = item.get("url", "")
                # Check if the URL contains any of the specified extensions or keywords
                if (any(ext in url for ext in EXTENSIONS) or any(keyword in url.lower() for keyword in KEYWORDS)):
                    result = item.get("result", {})
                    urlworker = result.get("urlworker", {})
                    ip = urlworker.get("ip")
                    http_code = urlworker.get("http_code")
                    
                    # Append the filtered data to the results list
                    filtered_results.append({
                        "domain": domain,
                        "url": url,
                        "ip": ip,
                        "http_code": http_code
                    })
            
            print(f"{Fore.GREEN}Processed page {page} for domain {domain}. Found {len(filtered_results)} matching URLs so far.{Style.RESET_ALL}")
        
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Error fetching data from page {page} for domain {domain}: {e}{Style.RESET_ALL}")
            break
    
    return filtered_results

def process_domains_from_file(file_path, max_pages=5):
    # Read domains/subdomains from the file
    with open(file_path, "r") as file:
        domains = [line.strip() for line in file.readlines() if line.strip()]
    
    # Process each domain/subdomain
    all_results = []
    for domain in domains:
        print(f"{Fore.CYAN}Processing domain: {domain}{Style.RESET_ALL}")
        results = fetch_and_extract_data(domain, max_pages)
        all_results.extend(results)
    
    return all_results

def print_results(extracted_data):
    if extracted_data:
        print(f"{Fore.MAGENTA}Found {len(extracted_data)} URLs with matching extensions or keywords:{Style.RESET_ALL}")
        for entry in extracted_data:
            print(f"{Fore.BLUE}Domain: {entry['domain']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}URL: {entry['url']}")
            print(f"{Fore.YELLOW}IP: {entry['ip']}")
            print(f"{Fore.GREEN}HTTP Code: {entry['http_code']}")
            print("-" * 50)  # Separator for readability
    else:
        print(f"{Fore.RED}No URLs found with the specified extensions or keywords.{Style.RESET_ALL}")

# Display the banner
display_banner()

# Example usage
file_path = "domains.txt"  # Path to the file containing domains/subdomains
extracted_data = process_domains_from_file(file_path)

# Print the filtered results
print_results(extracted_data)
