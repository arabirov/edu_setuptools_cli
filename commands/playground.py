import click


@click.group()
def hello():
    pass


@hello.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f'Hello, {name}!')
