This is a simple module for formating multiline
strings and docstrings in python.

# Usage

For simple strings you can use the `LLSTRIP` constant and
substraction.

``` python
from llstrip import LLSTRIP

foo = '''bla bla bla
         bla bla bla
         bla bla bla''' - LLSTRIP
```

For functions you can use the `llstripdec` decorator


``` python
from llstrip import llstripdec

@llstripdec
def foo(bar):
    '''bla bla bla
       bla bla bla
       bla bla bla'''
     pass
```

# License

Apache License 2.0
