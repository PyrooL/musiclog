"""
MusicBrainz API interface functions
Only access musicbrainzngs package directly from here
"""

import musicbrainzngs

musicbrainzngs.set_useragent("MusicLog", "0.1" "lm11887 [AT] gmail.com")

def search_album(search_string: str, limit : int = 10):
    try:
        results = musicbrainzngs.search_release_groups(search_string, limit = limit)['release-group-list']

        # todo: variable ext:score threshold? I think this is a score of how well the search matches
        albums = [r for r in results if (int(r['ext:score']) > 65 and 'type' in r.keys() and r['type'] in ['Album', 'EP'])]
        return albums
    except musicbrainzngs.NetworkError:
        print("Network error: could not search MusicBrainz database.")
        return []

    return results

def get_from_mbid(mbid):
    return musicbrainzngs.get_release_group_by_id(mbid, includes=['artist-credits', 'tags'])['release-group']
