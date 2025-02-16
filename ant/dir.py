# ruff: noqa: D100,S311

# Standard
import enum


class Dir(enum.Enum):
    """Direction of movement."""

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
