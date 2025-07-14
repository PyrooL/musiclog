import click
from commands import search, list_albums, sync_lastfm, add_manual
from core import logic

@click.group()
def main_cli():
    """MusicLog: A lightweight music logging tool"""
    pass

main_cli.add_command(search.search)
main_cli.add_command(list_albums.cmd_list_albums)
main_cli.add_command(sync_lastfm.sync_lastfm)
main_cli.add_command(add_manual.cmd_add_manual)

if __name__ == "__main__":
    main_cli()
