import click
from core.logic import search_album, add_album
from core.models import status_config

@click.command(name='search')
@click.argument("search_string")
@click.option("--limit", 'limit', default=10)
def cmd_search(search_string: str, limit):
    """Search MusicBrainz for an album"""

    click.echo(f'Searching MusicBrainz for albums that match "{search_string}"...')
    search_results = search_album(search_string, limit)
    click.echo(f"Found {len(search_results)} releases. (Max = {limit}, set with --limit).\n")

    if not search_results:
        click.echo("No results found!") # unlikely lol
        return

    album = None
    offset = 0
    for i, album in enumerate(search_results, start=1):
        click.echo(f" [{i}] {str(album)}")
        click.echo("")

    album_index = click.prompt("Add a release from the results to your collection (0 to skip)", type = click.Choice([i for i in range(len(search_results)+1)]), show_choices=False)

    if album_index in range(1,len(search_results)+1):
        status_index = click.prompt(status_config['status_prompt'], type = click.Choice([i for i in range(len(status_config['default_statuses']))]), show_choices=False)
        status = status_config['default_statuses'][status_index]
        album = search_results[album_index-1]
        album.status = status
        add_album(album)
        


