# -*- coding: utf-8 -*-

"""
    pyeez.window
    ~~~~~~~~~~~~

    This module implements the window class.

    :copyright: (c) 2016 by Mehdy Khoshnoody
    :license: GPLv3, see LICENSE for more details.
"""
import time
import contextlib
import curses
import threading

class Window(object):
    """
        Window is a part of the screen that can be used seperately
    :param name: the window name
    :param f: the function to be called on each loop to update the window
    :param topLeft: a tuple pointing to the top left corner of the window
    :param bottomRight: a tuple pointing to the bottom right corner of the window
    """

    def __init__(self, name, f, topLeft, bottomRight, **conf):
        if topLeft[0] >= bottomRight[0] or topLeft[1] >= bottomRight[1]:
            raise ValueError("wrong values for view corneres")

        self.name = name
        self.f = f
        self._topLeft = topLeft
        self._bottomRight = bottomRight
        self._lines = bottomRight[1] - topLeft[1]
        self._cols = bottomRight[0] - topLeft[0]
        self._window = curses.newwin(self._lines,
                                     self._cols,
                                     self._topLeft[1],
                                     self._topLeft[0])
        self._conf = {k.upper(): v for k, v in conf.items()}

        if 'REFRESH_RATE' in self._conf:
            threading.Thread(target=self._refreshPeriodically).start()

    def _refreshPeriodically(self):
        """
            Periodically refreshes the window.
            this function will be run in a different thread
        """
        while True:
            with self.refresh():
                self.f(self)
            time.sleep(self._conf['REFRESH_RATE'])

    def wrapper(self, *args, **kwargs):
        """
            Wraps the functions that are registered on the window to be
            run on each loop. it will inject the window object as an argument
        """
        return self.f(self, *args, **kwargs)

    @contextlib.contextmanager
    def refresh(self):
        """
            A context manager to prepare the window to do some actions on it
            and refresh the window afterward
        """
        self._window.clear()
        yield
        self._window.refresh()

    def echo(self, obj):
        """
            Prints on the window screen
        :param obj: the object to print on the window
        """
        with self.refresh():
            self._window.addstr(obj)

