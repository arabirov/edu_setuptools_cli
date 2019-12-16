import click

from commands import playground
from commands import wwg


@click.group()
def cli():
    pass


cli.add_command(playground.hello)
cli.add_command(wwg.poi_info)
cli.add_command(wwg.poi_image)