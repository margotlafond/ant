# Standard
import argparse

# Global constants
DEFAULT_STEPS = 10
DEFAULT_TILE_SIZE = 20
ANT_DEF_COLOR = (0, 0, 0)
DEFAULT_FPS = 3
MIN_FPS = 3
MAX_FPS = 30

def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Create parser & set description
    parser = argparse.ArgumentParser(
            description = "Langton's Ant.",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    # Checkerboard arguments
    parser.add_argument("--number-steps", "-S", type = int,
                        default = DEFAULT_STEPS,
                        help = "Number of steps made by the ant.")
    parser.add_argument("--tile-size", "-T", type = int,
                        default = DEFAULT_TILE_SIZE,
                        help="Tile size, in pixels")

    # Colors
    parser.add_argument("--ant-color", default = ANT_DEF_COLOR,
                        help="Color of the ant.")

    # Scores
    parser.add_argument("--state_file", "-F", type = str, default = "langton_state.yml",
                        help = "Path of the state file")

    # GUI
    parser.add_argument("--gui", "-G", type = bool, default = False,
                        help = "Path of the state file")
    
    # FPS
    parser.add_argument("--fps", type = int, default = DEFAULT_FPS,
                        help="Set the number of frames per second."
                        f" Must be between {MIN_FPS} and {MAX_FPS}.")

    # Verbose
    parser.add_argument("--verbose", "-v", dest = "verbose", action = "count", default = 0, 
                        help = "Verbose level. -v for information, -vv for debug.")

    # Parse
    args = parser.parse_args()
    
    # Run parser on command line arguments
    return args