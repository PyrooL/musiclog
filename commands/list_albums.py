import click
from core.logic import list_albums

@click.command(name='list')
@click.option('--status', 'status', type=str, help='Filter albums by status or tags (e.g. "listened", "want-to-listen"')
def cmd_list_albums(status = None):
    """List albums in your collection"""
    albums = list_albums(status)
    print(f"Found {len(albums)} albums")
    if len(albums) != 0:
        for album in albums:
            # todo: nicer print_album() method
            print(f"* {album.artist} - {album.title} ({album.release_year}) ({', '.join(album.tags)})")

