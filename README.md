# invigilate

A simple way to log any variables at runtime.

# Usage

Let's define a function to do some calculations. Sometimes we want to save local variables in this function, but don't know what variables are going to be important when. 

One solution is to log everything. This gets expensive. 

Another option is offered by this library. It lets you choose what variables to log at runtime.

```
from invigilate import Log

def run(num, monitor=None, save='data.csv'):
    logger = Log(monitor, update_every = 1)
    for i in range(num):
        x = i * 10
        y = x**2
        z = x / y
        logger.update(i, locals())
    logger.save(save)
    return z
```

A couple runtime examples.

```
    >>> run(10, monitor=('i', 'z'))
    # writes the saved data to 'data.csv'
```

```
    >>> run(10, monitor=('x', 'y', 'z'))
    # writes the saved data to 'data.csv'
```