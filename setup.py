from distutils.core import setup

setup(
    name='CINEMA-Server',
    version='0.0.1D',
    author="Noah G. Wood",
    author_email="ngwood111@gmail.com",
    packages=['cinema-core',],
    scripts=["bin/*",],
    url='',
    license='LICENSE.txt',
    description="CINEMA Is Noah's Extensible Mayfair Alternative",
    long_description=open("README.md").read(),
    install_requires=[
        "python-daemon >= 2.1.2",
    ],
)
