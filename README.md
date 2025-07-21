# MusicLog

A MusicBrainz-powered CLI music logger. 

## Install

```
git clone https://github.com/PyrooL/musiclog.git
cd musiclog
cp config/example_settings.py config/settings.py
pip install -r requirements.txt
```

## Usage

List albums in your collection

```python main.py list [--status FILTER_BY_STATUS]```

Search MusicBrainz DB for a release, prompts you to add to collection

```python main.py search "[QUERY STRING FOR MUSICBRAINZ DB]"```

Add an album directly from MusicBrainz ID

```python main.py add-from-mbid MBID1 [MBID2 MBID3...]```

