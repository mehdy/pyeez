# -*- coding: utf-8 -*-

from pyeez import Pyeez
import datetime

# creates an application
app = Pyeez(__name__)


# creates a window named "main"
# located at top left (10, 5) and bottom right (40, 20)
# that will be refreshed every second
@app.window("main", (10, 5), (40, 20), refresh_rate=1)
def main(w):
    w.echo("Now: {}".format(datetime.datetime.now().time()))

# creates a window named "word"
# that will be updated whenever "key_press" event happens
@app.on("key_press")
@app.window("word", (60, 5), (80, 20))
def typing(w, e):
    w.echo("key pressed: {}".format(e.data))

if __name__ == '__main__':
    app.run()
