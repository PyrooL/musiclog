import click
from core.models import Album, DEFAULT_STATUSES
from core.logic import add_album

status_prompt_text = 'Status: [1] Listened [2] Want to Listen [3] Favorite [4] Skip'

@click.command(name='add-manual')
@click.option('--artist', prompt = 'Artist')
@click.option('--title', prompt = 'Album name')
@click.option('--release-year', prompt = 'Release year')
@click.option('--status', prompt = status_prompt_text, type=click.Choice([str(i+1) for i in range(len(DEFAULT_STATUSES))]))
@click.option('--tags', prompt = 'Tags (comma-separated, optional)', default = '')
def cmd_add_manual(artist, title, release_year, status, tags):
    """Manually add an album to your collection"""
    tags_list = [t.strip() for t in tags.split("t") if t and tags is not None]
    add_album(artist=artist, title=title, release_year=release_year, status=DEFAULT_STATUSES[int(status)-1], tags = tags_list, source='user')

