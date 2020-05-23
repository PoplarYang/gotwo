#!/usr/bin/env python3
# coding=utf8

from .gotwo import ISSH, CONFIG_PATH

def main():
    ssh = ISSH(CONFIG_PATH)
    ssh.run()
