from db import db
from core.models import Album, DEFAULT_STATUSES

def add_album(artist, title, release_year, status, tags = ""):
    # does it make sense to pass an Album object or do the construction here?
    collection = db.load_collection()
    if status not in DEFAULT_STATUSES:
        print("WARNING: assigning non-default status")
    album = Album(artist=artist, title=title, release_year=release_year, status=status, tags = [t.strip() for t in tags.split(",") if t and tags is not None])
    if is_in_collection(album):
        print("Album already in collection!")
    else:
        collection.append(album)
    db.save_collection(collection)
    print(f"Added album: {artist} - {title} ({str(release_year)}) [{status}]")

def is_in_collection(album: Album):
    collection = db.load_collection()

    count = 0 
    for collection_album in collection:
        if album.artist.casefold == collection_album.artist.casefold() and album.title.casefold() == collection_album.title.casefold():
            count+=1

    if count > 1:
        print(f"WARNING: Detected {count} duplicates!")
    
    return count

def list_albums(status: None | str = None):
    # todo: parse a list of tags
    collection = db.load_collection()
    
    if status is None:
        return collection

    return [album for album in collection if album.status == status]
