# IPTV Playlist Manager

A simple Python CLI tool for managing M3U IPTV playlists — add, remove, list, filter, and export channels.

## Features

- Load and parse `.m3u` / `.m3u8` playlist files
- List all channels with name, group, and URL
- Filter channels by group or keyword
- Add / remove channels
- Export a cleaned playlist back to M3U format

## Requirements

- Python 3.8+

```bash
pip install -r requirements.txt
```

## Usage

```bash
# List all channels
python playlist_manager.py list --file playlists/my.m3u

# Filter by group
python playlist_manager.py list --file playlists/my.m3u --group "Sports"

# Search by keyword
python playlist_manager.py list --file playlists/my.m3u --search "BBC"

# Add a channel
python playlist_manager.py add --file playlists/my.m3u \
  --name "BBC One" --group "UK" --url "http://example.com/stream"

# Remove a channel by name
python playlist_manager.py remove --file playlists/my.m3u --name "BBC One"

# Export filtered group to a new file
python playlist_manager.py export --file playlists/my.m3u \
  --group "Sports" --output playlists/sports.m3u
```

## M3U Format

```
#EXTM3U
#EXTINF:-1 group-title="Group" tvg-name="Channel Name",Display Name
http://stream-url
```

## Project Structure

```
iptv1/
├── playlist_manager.py   # Main CLI
├── m3u_parser.py         # M3U parse/write logic
├── playlists/            # Store your .m3u files here
│   └── sample.m3u
├── requirements.txt
└── .gitignore
```
