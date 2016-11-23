Welcome To Pyeez!
=================

Quickstart
----------

**Pyeez** is great powerful python package for creating console applications like *top*.
it's simple and super easy to use. for example::

    import datetime

    from pyeez import Pyeez

    app = Pyeez(__name__)

    @app.window('clock', (5, 5), (20, 7), refresh_rate=1)
    def clock(w):
        w.echo('{}'.format(datetime.datetime.now().strftime('%T')))

    if __name__ == '__main__':
        app.run()

Installation and running::

    $ pip install pyeez
    $ python app.py

.. include:: contents.rst
