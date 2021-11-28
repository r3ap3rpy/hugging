### Welcome

This is a repo for some scripts related to the [hug](https://www.hug.rest/) API of python.

It ain't much but honest work.

Code for the first example.

``` bash
#hello_hug.py
from hello_hug import hello_world
hello_world(name = "Daniel")
```

Code for the second example.

``` bash
#hello_http.py
hug -f hello_http
# on linux you should install gunicorn then
gunicorn hello_http:__hug_wsgi__
```

Code for the third example.

``` bash
#hello_cli.py
hug -f .\hello_cli.py -c fibo 30
```