# -*- coding: utf-8 -*-

"""
    pyeez.event
    ~~~~~~~~~~~

    This module implements Pyeez events

    :copyright: (c) 2015 by Mehdy Khoshnoody.
    :license: GPLv2, see LICENSE for more details.
"""

class Event(object):
    """
        Event implements an event object which can be emitted
    """
    eventMapping = dict()

    def __init__(self, name, _type, data=None, *args, **kwargs):
        self.name = name
        self.type = _type
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def dispatch(self):
        """
            Emits the event to all event handlers
        """
        if self.name in Event.eventMapping:
            for eh in Event.eventMapping[self.name]:
                eh.handle(self)
        del self

    @staticmethod
    def on(name, *args, **kwargs):
        """
            A decorator to register the decorated function as an event handler
        :param name: the event name to listen on
        """
        def decorator(f):
            Event.register(name, f, *args, **kwargs)
            return f
        return decorator

    @staticmethod
    def register(name, f, *args, **kwargs):
        """
            Registers a function as an event handler
        :param name: the event to listen on
        :param f: the event handler function
        """
        eventHandler = EventHandler(name, f, *args, **kwargs)
        if name in Event.eventMapping:
            Event.eventMapping[name].append(eventHandler)
        else:
            Event.eventMapping[name] = [eventHandler]


class EventHandler(object):
    """
        Implements event handlers which will be called when an event is emitted
    :param name: the event name
    :param f: the function to be called when recieved an event
    """

    def __init__(self, name, f, *args, **kwargs):
        self.name = name
        self.f = f
        self.args = args
        self.kwargs = kwargs

    def handle(self, event):
        """
            Calls the registered function and passes the event object
        :param event: the recieved event object
        """
        return self.f(event, *self.args, **self.kwargs)
