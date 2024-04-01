import urllib.request
import sys
import json

tb = round(float(input("Please enter the number of terabytes worth of torrents you would like to download: ")), 2)
okay_to_download = input("Confirm download with Y / N: ")

if not okay_to_download == "Y":
    sys.exit()
    
with urllib.request.urlopen('https://annas-archive.org/dyn/generate_torrents?max_tb=' + str(tb) + '&format=json') as f:
    torrents = json.load(f)
    length = len(torrents)
    current = 1
    for i in torrents:
        urllib.request.urlretrieve(i["url"], "./torrents/" + i["display_name"])
        print(f"{current}/{length}: {i['display_name']} - {round(i['torrent_size']/1024)}kb ")
        current += 1
    f.close()