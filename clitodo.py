import click


@click.command()
def cli():
    print("Hello World!")


if __name__ == '__main__':
    cli()