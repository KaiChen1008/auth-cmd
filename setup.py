from setuptools import setup, find_packages

setup(
    name="auth",
    version="0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "re",
        "typing",
        "pathlib",
        "pyzbar",
        "pillow==10.3.0",
        "pyperclip",
        "hmac",
        "base64",
        "hashlib",
        "struct",
        "time",
        "csv",
    ],
    entry_points={
        "console_scripts": [
            "auth=auth.main:cli",  # command_name=module:function
        ],
    },
    author="Ken Lin",
    description="A TOTP authentication tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KaiChen1008/auth",  # If hosted on GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
