# invigilate

A simple way to log any variables at runtime.

# Usage

Let's define a nonsense function. It will to do some simple calculations. Imagine we want to log then save local variables from this function, but don't know which ones will be important when.

One solution is to log everything. This gets expensive. 

Another option is offered by this library. It lets you choose what variables to log at runtime.

```python 
from invigilate import Store

def nonsense(num, monitor=None, save='data.csv'):
    """Do some silly calculations."""
    store = Store(monitor, update_every = 1)
    for i in range(num):
        x = i * 10
        y = x**2
        z = x / y
        store.update(i, locals())
    store.save(save)
    return z
```

A couple runtime examples.

```python
    >>> nonsense(10, monitor=('i', 'z'))
    # writes the saved data to 'data.csv'
```

```python
    >>> nonsense(10, monitor=('x', 'y', 'z'))
    # writes the saved data to 'data.csv'
```
