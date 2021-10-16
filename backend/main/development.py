# pylint: disable=C0321,C0413
from gevent import monkey

monkey.patch_all()
import gevent
from werkzeug.serving import run_simple

from .apps import create_cards_app


GATEWAY_PORT = 9000


if __name__ == "__main__":
    gevent.joinall(
        [
            gevent.spawn(
                run_simple,
                "0.0.0.0",
                GATEWAY_PORT,
                create_cards_app(),
                use_reloader=True,
                use_debugger=True,
                threaded=True,
            ),
        ]
    )
