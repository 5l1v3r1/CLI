#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages
from factioncli.main import VERSION

PROJECT = 'Faction CLI'

if sys.argv[-1] == 'clean':
    if os.path.exists("./build"):
        os.system('rm -rf ./build')
    if os.path.exists("./dist"):
        os.system('rm -rf ./dist')
    if os.path.exists("./Faction_CLI.egg-info"):
        os.system('rm -rf ./Faction_CLI.egg-info')
    sys.exit()


try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Console application for interacting with Faction',
    long_description=long_description,

    author='The Faction Team',
    author_email='team@factionc2.com',

    url='https://github.com/factionc2/cli/',
    download_url='https://github.com/factionc2/cli/tarball/master',

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff', 'docker', 'sqlalchemy', 'requests', 'docker', 'bcrypt', 'psycopg2-binary', 'factionpy'],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'faction = factioncli.main:main'
        ],
        'faction.cli': [
            'setup = factioncli.commands.setup:Setup',
            'start = factioncli.commands.faction:Start',
            'stop = factioncli.commands.faction:Stop',
            'restart = factioncli.commands.faction:Restart',
            'reset = factioncli.commands.faction:Reset',
            'clean = factioncli.commands.clean:Clean',
            'status = factioncli.commands.status:Status',
            'new = factioncli.commands.new:New',
            'log = factioncli.commands.log:Log',
            'credentials = factioncli.commands.credentials:Credentials'
        ]
    },

    zip_safe=False,
)
