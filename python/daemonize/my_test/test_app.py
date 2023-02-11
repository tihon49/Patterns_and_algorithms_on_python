import logging


logging.basicConfig(level='DEBUG')
logger = logging.getLogger('test_logger')
logger.setLevel('DEBUG')

file_handler = logging.FileHandler('/tmp/test_log.log')
file_handler.setLevel(level='DEBUG')
logger.addHandler(file_handler)


def main():
    logger.warning('........Test........')


if __name__ == "__main__":
    main()
