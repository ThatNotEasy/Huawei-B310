import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import argparse
import re
from colorama import Fore, Style
import os
from datetime import datetime

RESULTS_FOLDER = "results"

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

def scan_links(url, html_content):
    if html_content:
        pattern = r'<a href="(.*?)"'
        links = re.findall(pattern, html_content)
        absolute_links = [urljoin(url, link) for link in links]
        return absolute_links
    else:
        return []

def process_url(url):
    html_content, status_code = get_response(url)
    
    if status_code is not None:
        if 200 <= status_code < 300:
            print_colored_message(f"Connection to {url} successful! (Status Code: {status_code})", Fore.GREEN)
            links = scan_links(url, html_content)
            print_colored_message(f"Links found for {url}:", Fore.CYAN)
            for link in links:
                print_colored_message(link, Fore.CYAN)

            save_successful_url(url, status_code)
        elif 300 <= status_code < 400:
            print_colored_message(f"Connection to {url} successful, but it's a redirection! (Status Code: {status_code})", Fore.YELLOW)
        else:
            print_colored_message(f"Connection to {url} failed with status code {status_code}. Please check the URL.", Fore.RED)
    else:
        print_colored_message(f"Connection to {url} failed. Please check the URL.", Fore.RED)

def save_successful_url(url, status_code):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(RESULTS_FOLDER, f"{status_code}_{timestamp}.txt")
    with open(filename, "a") as file:
        file.write(f"{url}\n")

def parse_args():
    parser = argparse.ArgumentParser(description="URL and Directory Scanner")
    parser.add_argument("-d", "--domain", required=True, help="Base URL to append paths from the wordlist")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the file containing paths to append to the base URL")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads for concurrent requests")

    args = parser.parse_args()

    if not args.domain.startswith("http://") and not args.domain.startswith("https://"):
        args.domain = "http://" + args.domain

    return args

def read_wordlist(wordlist_path):
    with open(wordlist_path, "r") as file:
        return file.read().splitlines()

def print_colored_message(message, color=Fore.WHITE, style=Style.RESET_ALL):
    print(f"{color}{message}{style}")

def main():
    args = parse_args()
    
    if not os.path.exists(RESULTS_FOLDER):
        os.makedirs(RESULTS_FOLDER)

    paths_to_append = read_wordlist(args.wordlist)
    combined_urls = [urljoin(args.domain, path) for path in paths_to_append]

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(process_url, combined_urls)

if __name__ == "__main__":
    main()
