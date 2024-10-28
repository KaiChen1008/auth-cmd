import click
import re
from typing import Tuple
from pathlib import Path
from pyzbar.pyzbar import decode
from PIL import Image
from auth.cmd.add import _add


@click.command()
@click.option(
    "--name",
    prompt="Enter a name for this token",
    help="Token name, e.g., 'GitHub token'.",
)
@click.option(
    "--qr_path",
    type=click.Path(exists=True),
    prompt="Enter the path to the QR code",
    help="Path to the QR code.",
)
def add_qr(name: str, qr_path: str) -> None:
    """
    Add a new token through a QR code.
    """
    try:
        secret, digit = decode_qr(Path(qr_path))
    except Exception as e:
        raise click.ClickException(f"Cannot decode QR code: {e}")

    try:
        _add(name, secret, digit)
    except Exception as e:
        raise click.ClickException(f"Add token failed: {e}")

    click.echo(f"Token {name} added successfully.")
    return


def decode_qr(p: Path) -> Tuple[str, int]:
    """
    Decode a QR code image.
    """
    try:
        img = Image.open(p)
    except Exception as e:
        raise ValueError(f"Open image failed: {e}")

    try:
        decoded_objects = decode(img)
    except Exception as e:
        raise ValueError(f"Decode image failed: {e}")

    if not decoded_objects:
        raise ValueError("No QR code detected.")

    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        try:
            secret = re.search("secret=([^&]*)", data).group(1)
        except Exception as e:
            raise ValueError(f"Invalid QR code data. {e}")

        try:
            digits = re.search("digits=([^&]*)", data).group(1)
        except Exception as _:
            click.echo("No digits found in QR code data. Using default(6).")
            return secret, "6"

        return secret, digits

    raise ValueError("Decode QR code failed.")
