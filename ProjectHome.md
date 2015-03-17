functools.partial allows for the currying of arguments.  However, being implemented in C, functools.partial objects are not pickleable.  This package implements a wrapper class for the partial objects, such that enables pickling of the objects.

You can download and install currypy using easy\_install as follows
```
easy_install currypy
```