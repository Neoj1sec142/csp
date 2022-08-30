from fabric import Connection
from fabric import SerialGroup

res = Connection('righthand.local', user="pi").run('uname -s', hide=True)
res.stdout
