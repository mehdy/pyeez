# -*- coding: utf-8 -*-

"""
    pyeez.app
    ~~~~~~~~~
    
    This module implements pyeez application class.
    
    :copyright: (c) 2015 by Mehdy Khoshnoody.
    :license: GPLv2, see LICENSE for more details.
"""

import curses

from .window import Window


class Pyeez(object):
    """
        The pyeez object implements a terminal-based application.

    :param name: application name
    :type name: str
    """

    def __init__(self, name):
        self.name = name
        self.windows = dict()

    def run(self):
        """
            Runs the application.
        """
        def runner(std_screen):
            self.windows['main'].c_window = std_screen
            self.windows['main'].show()

        curses.wrapper(runner)
        # runner(curses.initscr())

    def add_window(self):
        """
            Creates a new :class:`pyeez.window.Window` object.
        :return: a decorator to grab the window handler function
        """
        def decorator(f):
            self.windows[f.__name__] = Window(f.__name__, f)

        return decorator
