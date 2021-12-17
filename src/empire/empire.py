import logging
import sys

_logger = logging.getLogger(__name__)

LOG_FORMAT = "[%(asctime)s] %(levelname)s:%(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(log_level: int):
    """
    Setup basic logging

    :param log_level: minimum log level for emitting messages
    """
    logging.basicConfig(
        level=log_level, stream=sys.stdout, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT
    )


def main(args):
    setup_logging(logging.INFO)
    _logger.info("Starting empire...")


if __name__ == "__main__":
    main(sys.argv[1:])
