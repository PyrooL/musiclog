import click
from core.models import Album, status_config
from core.logic import add_from_mbid

@click.command(name='add-from-mbid')
@click.argument('mbid', required = True, nargs = -1)
@click.option('--status', prompt = status_config['status_prompt'], type = click.Choice([i for i in range(len(status_config['default_statuses']))]))
def cmd_add_from_mbid(mbid, status):
    """Add an album to your collection from its MusicBrainz ID"""
    for i in mbid:
        add_from_mbid(i, status_config['default_statuses'][status])
        print("")
