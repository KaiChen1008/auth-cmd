# Auth-Cmd

A TOTP (Time-based One-Time Password) authentication "**cmd"** tool.

## Installation

To install the package, run:

```python
pip install auth-cmd
```

## Usage

This tool provides several commands to manage TOTP tokens.

### Add a Token

To add a new token by qr-code

```sh
auth add-qr
```

You will be prompted to enter a name and qr code image path.

If you know the secret of a TOTP. You can add a new token by

```sh
auth add
```

### Generate a TOTP

To generate a TOTP for a specific token:

```sh
auth gen <name>
```

The generated TOTP will be copied to your clipboard.

### List Tokens

To list all existing tokens:

```sh
auth list
```

### Remove a Token

To remove a specific token:

```sh
auth remove <name>
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Author

Ken Lin
