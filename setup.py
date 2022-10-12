from setuptools import setup

setup(
    name="splatoon-painter",
    author="Phie Ash",
    description="A script to automatically paint images on Splatoon3 through a Linux system emulating a Switch Pro controller.",
    include_package_data=True,
    scripts=["splatoon-painter"],
    install_requires=[
        "opencv-python",
        "aioconsole",
        "dbus-python>=1.2.16,<1.4.0",
        "Flask>=1.1.2,<2.3.0",
        "Flask-SocketIO>=5.0.1,<5.4.0",
        "eventlet>=0.31,<0.34",
        "blessed>=1.17.10,<1.20.0",
        "pynput~=1.7.1",
        "psutil~=5.6.6",
        "cryptography>=3.3.2,<38.1.0",
    ]
)
