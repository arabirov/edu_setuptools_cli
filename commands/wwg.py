import click

from scripts import poi_messages


@click.group()
def wwg():
    pass


@wwg.command()
@click.option('--poi', default=0, help='POI ID')
@click.option('image', '-i', is_flag=True, required=False, type=click.STRING, default=False, help='Download POI Image')
def poi_info(poi, image):
    poi_info = poi_messages.poi_id_message(poi)
    if image:
        poi_image = poi_messages.poi_id_image(poi)
        response = (poi_info + "\n" + poi_image)
        click.echo(response)
    else:
        click.echo(poi_info)

# @wwg.command()
# @click.option('-i', is_flag=True, callback=poi_image, default=0, help='POI ID')
# def poi_image(poi):
#     poi_image = poi_messages.poi_id_image(poi)
#     click.echo(poi_image)
