# Anna's Torrents

Help preserve the largest truly open library in human history!
Python program to download torrent files that need seeding the most: go to [Anna's archive](https://annas-archive.org/torrents) for information.

Now linked on the [Anna's Archive](https://annas-archive.org/torrents#generate_torrent_list) website!

## Usage

- Run the program using python, and use the command line (CLI) and follow the prompts given.
- Torrents will be added to the `/torrents` directory, which will be created if it doesn't exist yet.
- The program will ask for the number of terabytes (TB) you would like to download and then will ask you to confirm.
- Information on progress and torrents will be provided as downloaded.

## What next?

This program only downloads the `.torrent` files, not the actual contents. `.torrent` files act as a table of contents: they contain metadata about the files and folders to be distributed. They also contain network locations of trackers and other properties of the torrent to help the torrent client. [Read more](https://en.wikipedia.org/wiki/Torrent_file)

To actually download and help seed the files, use a torrent client!
[qBittorrent](https://www.qbittorrent.org/) is recommended because it's open source, powerful, and reliable. Many other clients have issues such as malware, ads, and they can be less efficient.

## Disclaimer

By downloading and seeding these torrents, you are aiding in the distribution of material that may not be legal in your area of residence. These torrents are less hunted after compared to other material that would get you in trouble with anti-piracy agencies or the government, to be safe, use a VPN when you are downloading or seeding. Seed at your own risk.

## Example usage

```py
python download_torrents.py

Please enter the number of terabytes worth of torrents you would like to download (empty for no limit): 1
Confirm download with Y / N: y
Downloading torrent list...
Destination directory not found: creating now.
Beginning to download torrents.
1/6: annas_archive_data__aacid__ia2_acsmpdf_files__20240824T003059Z--20240824T003100Z.torrent - 348kb
2/6: annas_archive_data__aacid__ia2_acsmpdf_files__20240824T002415Z--20240824T002416Z.torrent - 436kb
3/6: annas_archive_data__aacid__duxiu_files__20240613T193041Z--20240613T193042Z.torrent - 479kb
4/6: c_996000.torrent - 177kb
5/6: s_621000.torrent - 62kb
6/6: annas_archive_meta__aacid__chinese_architecture_records__20241229T135101Z--20241229T135101Z.jsonl.seekable.zst.torrent - 3kb
Torrents downloaded. Use a BitTorrent client to join the network and start seeding.

```
