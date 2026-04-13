import os
import urllib.request, urllib.error
import sys
import json

DEST_DIR = "torrents"
DOMAINS = [
    'annas-archive.gl',
    'annas-archive.pk',
    'annas-archive.gd',
]

tb = input(
    "Please enter the number of terabytes of content to target (e.g., 0.05 for 50 GB, 10 for 10 TB; press Enter for no limit): ")

if not tb == '':
    tb = round(float(tb), 2)
okay_to_download = input("Confirm download with Y / N: ")

if not okay_to_download.upper() == "Y":
    sys.exit()

# Find operational mirror
domain = None
for url in DOMAINS:
    try:
        req = urllib.request.Request('https://' + url, method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as response:
            if 200 <= response.status < 400:
                print(f"Found operational mirror: {url}")
                domain = url
                break
    except urllib.error.URLError:
        continue
if not domain:
    print("No operational mirror found.")
    sys.exit()

print("Downloading torrent list...")

with urllib.request.urlopen(f'https://{domain}/dyn/generate_torrents?max_tb={tb}&format=json') as f:
    torrents = json.load(f)
    length = len(torrents)
    current = 1

    # Create the destination directory if it doesn't already exist
    if not os.path.exists(DEST_DIR):
        print("Destination directory not found: creating now.")
        os.mkdir(DEST_DIR)
    else:
        print("Destination directory found! Proceeding.")

    print("Beginning to download torrents.")
    for i in torrents:
        urllib.request.urlretrieve(
            i["url"], "./" + DEST_DIR + "/" + i["display_name"])
        print(
            f"{current}/{length}: {i['display_name']} - {round(i['torrent_size']/1024)}kb ")
        current += 1

    print("Torrents downloaded. Use a BitTorrent client to join the network and start seeding.")
    f.close()
