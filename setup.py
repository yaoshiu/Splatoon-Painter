from setuptools import setup

setup(
    name="splatoon-painter",
    include_package_data=True,
    version="1.0",
    author="Phie Ash",
    description="A script to automatically paint images on Splatoon3 through a Linux system emulating a Switch Pro controller.",
    install_requires=[
        "opencv-python", "nxbt[dbus-python]", "aioconsole", "dbus-python"
    ]
)
