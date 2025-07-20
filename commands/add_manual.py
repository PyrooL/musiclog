import click
from core.models import Album, status_config
from core.logic import add_album

@click.command(name='add-manual')
@click.option('--artist', prompt = 'Artist')
@click.option('--title', prompt = 'Album name')
@click.option('--release-year', prompt = 'Release year')
@click.option('--status', prompt = status_config['status_prompt'], type=click.Choice([i for i in range(len(status_config['default_statuses']))]))
@click.option('--tags', prompt = 'Tags (comma-separated, optional)', default = '')
def cmd_add_manual(artist, title, release_year, status, tags):
    """Manually add an album to your collection"""
    tags_list = [t.strip() for t in tags.split(",") if t and tags is not None]
    album = Album(artist=artist, title=title, release_year=release_year, status=status_config['default_statuses'][status], tags = tags_list, source='user')
    add_album(album)

