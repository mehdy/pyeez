# pyeez
[pyeez](https://pyeez.com) is a micro-framework to create console applications like **htop**.

## Installation
pyeez is easy to install. it has no dependencies.
* via **pip**:
```
$ pip install -U pyeez
```
* manual installation
```
$ git clone https://github.com/mehdy/pyeez.git
$ cd pyeez
$ python setup.py install
```
## Getting Started
building applications with pyeez is super easy.
write the code code below in a file (let's call it `awesome.py`) and save it.
```python
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

if __name__ == '__main__':
    app.run()
```
now just run the execute it.
```
$ python awesome.py
```
and now you have a realtime clock in terminal :)

## Contribution
feel free to open PRs :)
just keep in mind to update the documentation and tests if needed

### TODOs

* [ ] add more events
* [ ] add border option for windows
* [ ] add tests
* [ ] handle coloring
* [ ] handle windows movements
* [ ] add more examples
