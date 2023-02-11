import time
from daemonize import Daemonize

from my_test import test_app


def main():
    for _ in range(3):
        test_app.main()
        time.sleep(2)

daemon = Daemonize(
    app='test_daemon',
    pid='/tmp/test_pid.pid',
    action=main
)
daemon.start()
