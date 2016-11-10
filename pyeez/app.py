# -*- coding: utf-8 -*-

"""
    pyeez.app
    ~~~~~~~~~

    This module implements Pyeez application class.

    :copyright: (c) 2015 by Mehdy Khoshnoody.
    :license: GPLv2, see LICENSE for more details.
"""

import curses
import time
import inspect
import atexit
from threading import Thread

from .event import Event
from .window import Window


class Pyeez(object):
    """
        The Pyeez object implements a terminal-based application.

    :param name: application name
    """

    def __init__(self, name):
        self.name = name
        self._stdscr = curses.initscr()
        self._windows = dict()
        self.config = dict()

        curses.noecho()
        curses.cbreak()
        self._stdscr.refresh()

        atexit.register(self.exit)

    def exit(self):
        """
            Restores the normal mode of terminal
            Note::
                this will be called automatically on exit
        """
        curses.nocbreak()
        self._stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def getSize(self):
        """
            Get the screen size
        """
        return self._stdscr.getmaxyx()

    def addWindow(self, name, f, topLeft, bottomRight, **conf):
        """
            Create and append a new window with the given configurations
            to the app

        :param name: the window name
        :param f: the function to be called in every loop to update the window
        :param topLeft: a tuple of top left location of window
        :param bottomRight: a tuple of bottom right location of window
        """
        if name in self._windows:
            raise ValueError("different views can't have the same name")
        window = Window(name, f, topLeft, bottomRight, **conf)
        self._windows[name] = window
        return window.wrapper

    def window(self, name, topLeft, bottomRight, **conf):
        """
            A decorator to use the decorated function for
            :py:func:`Pyeez.addWindow`
        """
        def decorator(f):
            # TODO: handle generator functions too
            return self.addWindow(name, f, topLeft, bottomRight, **conf)
        return decorator

    def _consumeKeyboard(self):
        """
            waits for keyboard events and emit suitable events
        """
        while True:
            try:
                key = self._stdscr.getkey()
            except KeyboardInterrupt:
                exit()
            Event("key_press", "keyboard", key).dispatch()

    def on(self, eventName):
        """
            A decorator to register the decorated function as
            the event handler for a given event
        :param eventName: the event name to listen on
        """
        def decorator(f):
            Event.register(eventName, f)
            return f
        return decorator

    def run(self):
        """
            Runs the application.
        """
        self._stdscr.refresh()
        self._consumeKeyboard()

