import click
from core.logic import search_album

@click.command(name='search')
@click.argument("search_string")
@click.option("--limit", 'limit', default=0)
def cmd_search(search_string: str, limit):
    """Search MusicBrainz for an album"""
    print(f'Searching MusicBrainz for albums that match "{search_string}".')
    search_result = search_album(search_string, limit)
    if search_result:
        for album in search_result:
            album.display(show_status = False)
            print(f"MBID: {album.mbid}")
    else:
        print("No results!")

