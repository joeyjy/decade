import socket

# Import prod settimgs on prod host.
PRODUCTION_HOST = [
    'change me',
]

if socket.gethostname() in PRODUCTION_HOST:
    from .prod import *
else:
    from .dev import *
