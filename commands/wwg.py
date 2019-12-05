import click

from scripts import poi_messages


@click.group()
def wwg():
    pass


@wwg.command()
@click.option('--poi', default=0, help='POI ID')
def poi_info(poi):
    poi_info = poi_messages.poi_id_message(poi)
    click.echo(poi_info)
