import click
from core.models import Album, DEFAULT_STATUSES
from core.logic import add_from_mbid

status_prompt_text = 'Status: [1] Listened [2] Want to Listen [3] Skip'

@click.command(name='add-from-mbid')
@click.argument('mbid', required = True)
@click.option('--status', prompt = status_prompt_text, type = click.Choice([str(i+1) for i in range(len(DEFAULT_STATUSES))]))
def cmd_add_from_mbid(mbid, status):
    """Add an album to your collection from its MusicBrainz ID"""
    add_from_mbid(mbid, DEFAULT_STATUSES[int(status)-1])
