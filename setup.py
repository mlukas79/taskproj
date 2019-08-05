from setuptools import setup, find_packages
from taskproj import about


with open('name.txt', 'rt') as NM:
    NAME = NM.read().strip()

setup(
    name=NAME,
    version=about.__version__,
    packages=find_packages(exclude=('unit_tests*',)),
    license=about.__license__,
    description=about.__description__,

    author=about.__author__,
    author_email=about.__author_email__,
    platforms=['windows', 'linux'],
    install_requires=['pandas'],
    entry_points={
        'console_scripts': [
            'taskproj = taskproj.user_interface:main',
        ],
    }
)
