#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Create the group "input" that has direct access to /dev/input/event*, to facilitate textruct's mouse input

sudo groupadd rawinput
sudo tee /etc/udev/rules.d/99-rawinput.rules << '**EOF**' > /dev/null
KERNEL=="event*", NAME="input/%k", MODE="660", GROUP="rawinput"
**EOF**
#TODO: Add current user to rawinput group

#TODO: Look into using `mev` for mouse input. For nicer-looking output, use -E flag, for more detailed output use no flags. Also: Find out how to discern scrolling from movements