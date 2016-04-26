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
from threading import Thread


class Pyeez(object):
    """
        The Pyeez object implements a terminal-based application.

    :param name: application name
    :type name: str
    """

    def __init__(self, name):
        self.name = name
        self._window = None
        self._ui = None
        self._ui_handler = None
        self._ui_generator = None
        self._running = False
        self.config = dict()

    def run(self):
        """
            Runs the application.
        """

        def runner(std_screen):
            """
                curses call this function inside it's wrapper to run the
                application peacefully
            :param std_screen: the application's main screen
            """
            self._window = std_screen
            self._running = True
            try:
                self._update_ui(generator=self._ui_generator or False)
                # TODO: run the event loop
            except KeyboardInterrupt:
                self._running = False

        curses.wrapper(runner)

    def _update_ui(self, generator=None):
        if generator:
            def update(self):
                while self._running:
                    result = next(self._ui_generator)
                    self._window.clear()
                    self._window.addstr(result)
                    self._window.refresh()
                    time.sleep(self.config['REFRESH_RATE'])
        else:
            def update(self):
                while self._running:
                    result = self._ui_handler()
                    self._window.clear()
                    self._window.addstr(result)
                    self._window.refresh()
                    time.sleep(self.config['REFRESH_RATE'])
        Thread(target=update, args=(self,)).start()

    def update_ui(self):
        """
            Registers the UI updating function of application to be used when
            running application.
        :return: A decorator
        """

        def decorator(f):
            """
                Determines the function to see whether it's a generator
                function or not. And registers it properly.
            :param f: the UI updating function
            """
            if inspect.isgeneratorfunction(f):
                self._ui_generator = f()
            else:
                self._ui_handler = f
        return decorator
