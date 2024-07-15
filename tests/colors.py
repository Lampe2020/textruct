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
Shows test output for testing if the environment supports certain colour modes.
Heavily helped by https://en.wikipedia.org/wiki/ANSI_escape_code
"""

# nl='\n';print(''.join(f'''\033[38;5;{i}m\033[48;5;{i}m#\033[0m{nl if i in(15,*(n+15 for n in range(256-15) if not n%36))else''}'''for i in range(256))) # 256 colour capability test one-liner

print('16 colors:')
#TODO: Implement this!

print('\n256 colors:')
patternchange_borders_256_col:tuple[int] = (15, *((n + 15) for n in range(256 - 15) if not (n % 36)))
palette_256:str = ''
for i in range(256):
    palette_256 += f'\033[38;5;{i}m\033[48;5;{i}m#\033[0m'
    if i in patternchange_borders_256_col:
        palette_256 += '\n'
print(palette_256)

print(f'\n24-bit color:\n(only example colors as {2**24} different colors are possible)')
# fg: ESC[38;2;⟨r⟩;⟨g⟩;⟨b⟩ m
# bg: ESC[48;2;⟨r⟩;⟨g⟩;⟨b⟩ m
palette_24bit:str = ''
#TODO: Implement this!