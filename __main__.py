#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright 2024 Christian Lampe
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
The loader for Textruct. Responsible for handling the argument parsing and launching of the game.
"""

from argparse import ArgumentParser
argparser:ArgumentParser = ArgumentParser(
    prog='textruct',
    description='An ASCII-rendered block game written in Python',
    epilog='NOTE: This game should not be run in a terminal with less than 22 rows and 80 '
           'columns, as it renders 3D graphics to the terminal, drastically reducing '
           'visual detail. It is recommended to run the game in the Linux TTY, as that is '
           'what the game is optimized for.',
    add_help=True   # Redundant (on by default), but written here as a note in case necessary to disable later on
)
# arg doc help line borders ↓                                                                                ↓
argparser.add_argument('-c', '--color-mode',
                       default='truecolor',
                       choices=[
                           'monochrome', '1-bit', '2',  # Set the color mode to monochrome
                           '16-color', '16',            # Set the color mode to 16-color
                           '256-color', '256',          # Set the color mode to 256-color
                           'truecolor', '24-bit', '16m' # Set the color mode to true color
                       ],
                       help='Set the color mode to use when outputting the game visuals.')
argparser.add_argument('-g', '--background',
                       default='color',
                       choices=['c', 'color', 'd', 'dark', 'l', 'light'],
                       help='If "dark" is specified (default), textruct will assume the background color to '
                            'be dark and only color the characters, not their background. If "light" is '
                            'specified, textruct will assume the background color to be light and only color '
                            'the characters, not their background. If "color" is specified, the background '
                            'color will also be used if the color mode allows for it. Each value can be '
                            'abbreviated to its initial.'
                       )
argparser.add_argument('-b', '--black-and-white',
                       action='store_true',
                       help="Only output shades of grey. Doesn't do anything in monochrome color mode as "
                            'only black and white are used in that mode anyway.'
                       )
argparser.add_argument('-p', '--pixel-mode',
                       action='store_true',
                       help='Enable pixel mode. Requires UTF-8 support. Uses the top-half block character to '
                            'separate each character into two pixels and then colors in the back- and '
                            'foreground accordingly. "-g" or "--background" is ignored in pixel mode, except '
                            'in monochrome color mode where it also uses the bottom-half block character.'
                       )
argparser.add_argument('-s', '--server',
                       action='store_true',
                       help='Go into server mode. Instead of game visuals, an interactive console is shown. '
                            'Other game clients can connect to this server, provided they can see it in the '
                            'network, instead of launching their own internal server to play.'
                       )
argparser.add_argument('-w', '--world',
                       help="Specify a world name or server address to play on. If the world doesn't exist "
                            'yet, the world creation screen is shown, prepopulated with the specified world '
                            'name. To specify a server, supply a server address with the "txc://" protocol. '
                            'If server mode is activated, this parameter is needed to specify the world to '
                            'be served. If none is specified, the last-served world is selected, if that is '
                            'not possible the last-played world is selected, if that is not possible a new '
                            'world is generated with random parameters and stored under a randomly-generated '
                            'name.'
                       )
print(argparser.parse_args())   #debug
