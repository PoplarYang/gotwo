#!/usr/bin/env python
# coding: utf8
from asciimatics.screen import Screen
from time import sleep


def demo(screen):
    screen.print_at('Hello world!', 20, screen.height // 2 - 8)
    screen.print_at(u'☎ Call me!', 0, 1)
    screen.refresh()
    sleep(10)


Screen.wrapper(demo)