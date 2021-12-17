import logging
import sys

_logger = logging.getLogger(__name__)


def setup_logging(log_level: int):
    """
    Setup basic logging

    :param log_level: minimum log level for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s: %(message)s"
    logging.basicConfig(
        level=log_level, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    setup_logging(logging.INFO)
    _logger.info("Starting empire...")


if __name__ == "__main__":
    main(sys.argv[1:])
