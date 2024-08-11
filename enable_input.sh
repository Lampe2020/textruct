#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Create the group "input" that has direct access to /dev/input/event*, to facilitate textruct's mouse input

sudo groupadd rawinput
sudo tee /etc/udev/rules.d/99-rawinput.rules << '**EOF**' > /dev/null
KERNEL=="event*", NAME="input/%k", MODE="660", GROUP="rawinput"
**EOF**
#TODO: Add current user to rawinput group