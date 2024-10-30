<p align="center">
  <img src="assets/logo.2.png" height="256">
  <!-- <h1 align="center">Auth CMD</h1> -->
  <p align="center">A secure and privacy-focused command-line tool for two-factor authentication (2FA) and Time-based One-Time Passwords (TOTP).</p>
</p>


> [!IMPORTANT]  
> To ensure the safety of your authentication data, please use auth-cmd only on a secure, private computer.


<div align="center">
  <video controls autoplay src="https://github.com/user-attachments/assets/805c9174-1051-4c1a-a554-7997129356e7" height="256" />
</div>

## Installation

### Install zbar

- **Ubuntu**

```sh
  sudo apt update && sudo apt install -y libzbar-dev
```

- **MacOS**

```sh
  brew install zbar
```

  - If `auth-cmd` cannot locate the `zbar` library after installation, try creating a symbolic link for the zbar shared library:
  - [reference](https://stackoverflow.com/questions/63217735/import-pyzbar-pyzbar-unable-to-find-zbar-shared-library/71904987#71904987)

```sh
  mkdir ~/lib
  ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib
```

- **Windows**
  - Download the installer from the [zbar homepage](https://zbar.sourceforge.net/download.html) and follow the instructions provided.

### Install Package

```sh
pip install auth-cmd
```

## Usage

This tool provides several commands to manage TOTP tokens.

### Add a Token

To add a new token by a QRcode

```sh
auth add-qr
```

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

**Want Faster? Create an alias to speed up the process!**

```sh
alias gen='auth gen'
# or
alias g='auth gen'
```

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

Ken Lin (<1038790@gmail.com>)

<a href="https://buymeacoffee.com/kaichen1008
" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

