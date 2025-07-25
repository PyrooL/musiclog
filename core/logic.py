from db import db
from core.models import Album, status_config
from api import musicbrainz

def is_in_collection(album: Album):
    collection = db.load_collection()
    count = 0 
    for collection_album in collection:
        if album.mbid is not None and collection_album.mbid == album.mbid:
            count += 1
            continue
        if album.artist.casefold == collection_album.artist.casefold() and album.title.casefold() == collection_album.title.casefold():
            count+=1
    if count > 1:
        print(f"WARNING: Detected {count} duplicates!")
    return count

def add_album(album: Album):
    # album = Album(artist=artist, title=title, release_year=release_year, status=status, tags = tags, source = source, mbid = mbid)
    collection = db.load_collection()
    if album.status not in status_config['default_statuses']:
        print("WARNING: assigning non-default status")
    if is_in_collection(album) > 0:
        print("Album already in collection!")
    else:
        print(f"Added album: {str(album)}")
        collection.append(album)
        db.save_collection(collection)

def list_albums(status: None | str = None):
    # todo: parse a list of tags
    collection = db.load_collection()
    if status is None:
        return collection
    return [album for album in collection if album.status == status]

def search_album(search_string: str, limit: int = 10):
    search_result = musicbrainz.search_album(search_string, limit=limit)
    result_parsed = [parse_mb_album(r) for r in search_result]
    return result_parsed

def add_from_mbid(mbid, status = "uncategorized"):
    mb_album = musicbrainz.get_from_mbid(mbid)
    if mb_album:
        album = parse_mb_album(mb_album)
        album.mbid = mbid
        album.source = 'user'
        album.status = status
        add_album(album)

def parse_mb_album(mb_album) -> Album:
    title = mb_album['title']
    artist = mb_album['artist-credit-phrase']
    if 'first-release-date' in mb_album.keys(): 
        # i guess i should handle full release dates at some point
        release_year = mb_album['first-release-date'].split('-')[0] 
    else:
        release_year = -1
        print("No release year found!")
    mbid = mb_album['id']
    album = Album(title = title, artist = artist, release_year = release_year, mbid = mbid, source='user')
    if 'tag-list' in mb_album.keys():
        album.tags = [tag['name'] for tag in sorted(mb_album['tag-list'], key=lambda x: x['count'], reverse=True)][0:10] # surprised this indexing doesn't throw an error lol
    else:
        album.tags = []
        # print("No tags found!")

    return album

def find_broken_albums():
    # todo: fill this out a bit more
    collection = db.load_collection()
    for album in collection:
        if album.release_year == -1:
            print("Year")
            album.display() # placeholder
        # etc
        if album.status == status_config['default_statuses'][-1]:
            print("Uncategorized")
            album.display() # placeholder
