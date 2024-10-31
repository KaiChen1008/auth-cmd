from setuptools import setup, find_packages

setup(
    name="auth-cmd",
    version="0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "regex",
        "typing",
        "pathlib",
        "pyzbar",
        "pillow",
        "pyperclip",
        "pybase64",
    ],
    entry_points={
        "console_scripts": [
            "auth=auth.main:cli",  # command_name=module:function
        ],
    },
    author="Ken Lin",
    description="A 2FA/TOTP authentication tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KaiChen1008/auth-cmd",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
