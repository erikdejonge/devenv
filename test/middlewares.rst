===========
Middlewares
===========

.. module:: werkzeug.wsgi

Middlewares wrap applications to dispatch between then or provide
additional request handling.  Additionally to the middlewares documented

    hello world


here, there is also the :class:`DebuggedApplication` class that is
implemented as a WSGI middleware.

.. autoclass:: SharedDataMiddleware
   :members: is_allowed

.. autoclass:: DispatcherMiddleware

Also there's the …

.. autofunction:: werkzeug._internal._easteregg

and a piece of code

.. code-block:: python

    def correct_codeblocks(mdfile):
       inbuf = [x.rstrip().replace("\t", "    ") for x in open(mdfile)]
       outbuf = []
       cb = False
       for l in inbuf:
           if l.startswith("    ") and not l.endswith(";"):
               if not cb:
                   outbuf.append("```python")
               cb = True
           else:
               if cb is True:
                   cb = False
                   outbuf.append("```")
           if cb is True:
               l = l.replace("    ", "", 1)
           outbuf.append(l)
       open(mdfile, "w").write("\n".join(outbuf))
