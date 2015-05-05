Nameko
======

![image](https://secure.travis-ci.org/onefinestay/nameko.png?branch=master)

```
:target: <http://travis-ci.org/onefinestay/nameko>
```
*[nah-meh-koh]*

A nameko service is just a class:

``` python
# helloworld.py

from nameko.rpc import rpc

class GreetingService(object):
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
```

You can run it in a shell:

``` bash
$ nameko run helloworld
starting services: greeting_service
...
```

And play with it from another:

``` bash
$ nameko shell
>>> n.rpc.greeting_service.hello(name="Matt")
u'Hello, Matt!'
```

Features
--------

> -   AMQP RPC and Events (pub-sub)
> -   HTTP GET, POST & websockets
> -   CLI for easy and rapid development
> -   Utilities for unit and integration testing

Getting Started
---------------

> -   Check out the [documentation](http://nameko.readthedocs.org).

Support
-------

> -   Join the mailing list
> -   Find us on IRC

Contribute
----------

> -   Fork the repository
> -   Raise an issue or make a feature request

License
-------

Apache 2.0. See LICENSE for details.
