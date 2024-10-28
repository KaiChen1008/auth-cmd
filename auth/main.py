import click
from auth.cmd.add import add
from auth.cmd.add_qr import add_qr
from auth.cmd.list import list
from auth.cmd.remove import remove
from auth.cmd.gen import gen


@click.group()
def cli():
    pass


if __name__ == "__main__" or __name__ == "auth.main":
    cli.add_command(add)
    cli.add_command(add_qr)
    cli.add_command(list)
    cli.add_command(remove)
    cli.add_command(gen)

    cli()
