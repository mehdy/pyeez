# -*- coding: utf-8 -*-

"""
    pyeez.window
    ~~~~~~~~~~~~
    
    This module implements pyeez window class
    
    :copyright: (c) 2015 by Mehdy Khoshnoody.
    :license: GPLv2, see LICENSE for more details.
"""

import curses


class Window(object):
    """
        The Window object implements a window to select a specific part of
        the whole window.

    :param name: window name
    :type name: str
    :param handler: handler generator that shows the content in the window
    :type handler: callable
    """

    def __init__(self, name, handler):
        self.name = name
        self.handler = handler()
        self.c_window = None

    def init(self):
        """
            Initialize the window.
        :return:
        """
        self.c_window = curses.newwin() if not self.c_window else self.c_window

    def show(self):
        """
            Runs the handler to show the content in the window
        :return:
        """
        self.init()
        self.update()

    def update(self):
        """
            Updates the screen and
        :return:
        """
        while True:
            self.c_window.clear()
            self.c_window.refresh()
            try:
                next(self.handler)
            except StopIteration:
                break
