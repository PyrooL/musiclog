"""
MusicBrainz API interface functions
Only access musicbrainzngs package directly from here
"""

import musicbrainzngs

musicbrainzngs.set_useragent("MusicLog", "0.1" "lm11887 [AT] gmail.com")

def search_album(search_string: str, limit : int = 5):
    try:
        results = musicbrainzngs.search_release_groups(search_string, limit = limit)['release-group-list']
        albums = [r for r in results if r['type'] in ['Album', 'EP']]
        print(f"Found {len(albums)} matching albums")
        return albums
    except musicbrainzngs.NetworkError:
        print("Network error: could not search MusicBrainz database.")
        return []

    return results

def get_from_mbid(mbid):
    return musicbrainzngs.get_release_group_by_id(mbid, includes=['artist-credits', 'tags'])['release-group']

def print_release_group(release_group):
    # can be made prettier
    # not sure if this method should be here or in utils/ or core/logic.py
    
    for key in release_group:
        print(f"{key}: {release_group[key]}")
