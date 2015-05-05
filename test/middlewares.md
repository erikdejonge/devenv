Middlewares
===========

Middlewares wrap applications to dispatch between then or provide additional request handling. Additionally to the middlewares documented here, there is also the DebuggedApplication class that is implemented as a WSGI middleware.

```docutils 
.. autoclass:: SharedDataMiddleware 
   :members: is_allowed
```
```
.. autoclass:: DispatcherMiddleware
```
Also there's the …

```
.. autofunction:: werkzeug._internal._easteregg
```