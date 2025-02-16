# ruff: noqa: D100,S311

# Standard
import logging
import colorlog

# First party
from .cmd_line import read_args
from .game import Game

# Constants
HEIGHT = 500
WIDTH = 300


def main() -> None: # noqa: D103

    logger = logging.getLogger("foo")
    color_fmt = colorlog.ColoredFormatter(
    "%(log_color)s[%(asctime)s][%(levelname)s] %(message)s",
    log_colors={
        "DEBUG": "yellow",
        "INFO": "green",
        "WARNING": "purple",
        "ERROR": "red",
        "CRITICAL": "red",
        })
    color_handler = colorlog.StreamHandler()
    color_handler.setFormatter(color_fmt)
    logger.addHandler(color_handler)

    # Read command line arguments
    args = read_args()

    # Start game
    if args.verbose == 1:
        logger.setLevel(logging.INFO)
    elif args.verbose == 2:
        logger.setLevel(logging.DEBUG)

    # Start game
    Game(nb_steps = args.number_steps, tile_size = args.tile_size, 
         fps = args.fps, ant_color = args.ant_color, score_file = args.score_file,
         gui = args.gui, logger_obj = args.logger_obj, width = WIDTH, height = HEIGHT)
