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


@wwg.command()
@click.option('--poi', default=0, help='POI ID')
def poi_image(poi):
    poi_image = poi_messages.poi_id_image(poi)
    click.echo(poi_image)
