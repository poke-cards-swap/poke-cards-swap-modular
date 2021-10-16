# pylint: disable=C0321,C0413,C0411,E0401,C0412
from gevent import monkey; monkey.patch_all()

import os

import gevent
from gevent.pywsgi import WSGIServer

from .apps import create_cards_app_with_proxy


GATEWAY_HOST = os.environ.get('GATEWAY_HOST', '0.0.0.0')
GATEWAY_PORT = os.environ.get('GATEWAY_PORT', 9000)


if __name__ == '__main__':

    http_server = WSGIServer((GATEWAY_HOST, GATEWAY_PORT), create_cards_app_with_proxy())

    try:
        gevent.joinall([
            gevent.spawn(http_server.serve_forever),
        ])
    except KeyboardInterrupt:
        print('Exiting')