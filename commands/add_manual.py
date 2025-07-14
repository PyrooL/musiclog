import click
from core.models import Album, DEFAULT_STATUSES
from core.logic import add_album

status_prompt_text = 'Status [1] Listened [2] Want to Listen [3] Favorite [4] Skip'

@click.command(name='add-manual')
@click.option('--artist', prompt = 'Artist')
@click.option('--title', prompt = 'Album name')
@click.option('--release-year', prompt = 'Release year')
@click.option('--status', prompt = status_prompt_text, type=click.Choice([str(i+1) for i in range(len(DEFAULT_STATUSES))], case_sensitive=False))
@click.option('--tags', prompt = 'Tags (comma-separated, optional)', default = '')
def cmd_add_manual(artist, title, release_year, status, tags):
    """Manually add an album to your collection"""
    
    if tags is None:
        tags = ''
        
    add_album(artist=artist, title=title, release_year=release_year, status=DEFAULT_STATUSES[int(status)-1], tags = tags)

def parse_status(status) -> str:
    # I wonder if it's more elegant to have a an AlbumStatus dataclass or methods to handle the status in the Album class
    while True:
        if str(status).isdigit():
            status_index = int(status)
            if 1 <= status_index <= len(DEFAULT_STATUSES):
                return DEFAULT_STATUSES[status_index-1]

        print(f"Please enter a number from 1 to {len(DEFAULT_STATUSES)}")

        status = click.prompt(status_prompt_text)

