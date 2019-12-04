import click

from py import playground


@click.group()
def cli():
    pass


cli.add_command(playground.hello)
