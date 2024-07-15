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
The ASCII shader for textruct, converts a pixel image to ASCII art and allows for modifications to the output buffer.
"""

class ASCIIRenderer:
    """
    Render pixels to ASCII art.
    """
    color_bit_depth:int = 24
    pixel_mode:bool = False
    background:str = 'd'
    #TODO: Define all the default values and then implement all this!