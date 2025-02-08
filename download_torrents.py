import os
import urllib.request
import sys
import json

DEST_DIR = "torrents"

tb = input(
    "Please enter the number of terabytes worth of torrents you would like to download (empty for no limit): ")

if not tb == '':
    tb = round(float(input(
        "Please enter the number of terabytes worth of torrents you would like to download: ")), 2)
okay_to_download = input("Confirm download with Y / N: ")

if not okay_to_download == "Y":
    sys.exit()

print("Downloading torrent list...")

with urllib.request.urlopen('https://annas-archive.org/dyn/generate_torrents?max_tb=' + str(tb) + '&format=json') as f:
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
    f.close()
