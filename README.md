 # URL and Directory Scanner

This Python script scans a given base URL with a list of paths to identify valid URLs and their status codes. It uses multithreading for concurrent requests and saves the successful URLs to a results folder.

## Prerequisites

- Python 3 or later
- `requests` library
- `colorama` library

## Usage

```
python scanner.py -d <base_url> -w <wordlist_path> -t <num_threads>
```

**Arguments:**

- `-d`: Base URL to append paths from the wordlist.
- `-w`: Path to the file containing paths to append to the base URL.
- `-t`: Number of threads for concurrent requests (default: 5).

## Step-by-Step Explanation

### 1. Import Necessary Libraries

```python
import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import argparse
import re
from colorama import Fore, Style
import os
from datetime import datetime
```

### 2. Define Constants

```python
RESULTS_FOLDER = "results"
```

### 3. Define Helper Functions

#### `get_response(url)`:

- Sends a GET request to the specified URL.
- Handles redirects and exceptions.
- Returns the HTML content and status code of the response.

```python
def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        location_header = response.headers.get('Location')
        if location_header:
            print_colored_message(f"Redirected to: {location_header}", Fore.YELLOW)

        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
        print_colored_message(f"Error connecting to {url}: {e}", Fore.RED)
        return None, None
```

#### `scan_links(url, html_content)`:

- Parses the HTML content for links.
- Returns a list of absolute links.

```python
def scan_links(url, html_content):
    if html_content:
        pattern = r'<a href="(.*?)"'
        links = re.findall(pattern, html_content)
        absolute_links = [
