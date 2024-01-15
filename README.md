 # URL and Directory Scanner

This README file offers a comprehensive explanation of two Python scripts. The first script is designed to create a tar archive of files on a remote server and subsequently transfer that archive to a local machine. The second script scans a provided base URL with a list of paths, identifying valid URLs and their corresponding status codes. The script employs multithreading to handle concurrent requests and stores successful URLs in a results folder.

**Prerequisites:**

- SSH access to the remote server with root privileges.
- SCP (Secure Copy) utility installed on both the remote server and the local machine.

**Step-by-Step Explanation of the Code:**

**1. SSH Command:**

```shellscript
ssh -p 22 root@192.168.8.1 "cd /online/AIO_LoveTacome/GUI && tar czf archive.tar.gz *"
```

- This command establishes an SSH connection to the remote server with the IP address `192.168.8.1`. The `-p 22` option specifies the port number for the SSH connection, which is typically 22.
- The `root` user is used to log in to the remote server.
- The command inside the double quotes is executed on the remote server.
- The `cd` command navigates to the directory `/online/AIO_LoveTacome/GUI` on the remote server.
- The `tar` command is used to create a compressed tar archive named `archive.tar.gz` of all the files in the current directory (`*`). The `c` option creates a new archive, `z` indicates gzip compression, and `f` specifies the output file name.

**2. SCP Command:**

```shellscript
scp -P 22 root@192.168.8.1:/online/AIO_LoveTacome/GUI/archive.tar.gz /path/to/local/directory
```

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
        absolute_links = []
```



- This command uses SCP to securely copy the `archive.tar.gz` file from the remote server to the local machine.
- The `-P 22` option again specifies the port number for the SSH connection.
- The source path `/online/AIO_LoveTacome/GUI/archive.tar.gz` indicates the location of the archive file on the remote server.
- The destination path `/path/to/local/directory` specifies the
