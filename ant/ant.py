# First party
import typing
from .dir import Dir
from .tile import Tile
from .board import Board

# Third party
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
BLUE = (193, 225, 255)

class Ant:
    """The ant."""

    def __init__(self, x: int, y: int, direction: Dir) -> None:
        self._x = x # Coordinate x of the tile where the ant is
        self._y = y # Coordinate y of the tile where the ant is
        self._dir = direction

    @property
    def dir(self) -> Dir:
        """Ant direction."""
        return self._dir

    @dir.setter
    def dir(self, direction: Dir) -> None:
        self._dir = direction

    def turn_right(self) -> None:
        """Turns the ant right."""
        if self._dir == Dir.UP:
            self._dir = Dir.RIGHT
        elif self._dir == Dir.RIGHT:
            self._dir = Dir.DOWN
        elif self._dir == Dir.DOWN:
            self._dir = Dir.LEFT
        elif self._dir == Dir.LEFT:
            self._dir = Dir.UP

    def turn_left(self) -> None:
        """Turns the ant left."""
        if self._dir == Dir.UP:
            self._dir = Dir.LEFT
        elif self._dir == Dir.RIGHT:
            self._dir = Dir.UP
        elif self._dir == Dir.DOWN:
            self._dir = Dir.RIGHT
        elif self._dir == Dir.LEFT:
            self._dir = Dir.DOWN

    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the ant."""
        return self._x
    
    @property
    def y(self) -> int:
        """The y coordinate (i.e.: line index) of the ant."""
        return self._y

    def move(self, tile: Tile) -> None:
        """Moves the ant : first checks the tile color, then turns, then changes the tile color, and then moves"""
        # Changes the color and direction
        if tile.color == BLACK:
            self.turn_left()
            tile.color = BLUE # This tile is white but has been visited
        else:
            self.turn_right()
            tile.color = BLACK

        # Moves the ant
        self._x += self._dir[0]
        self._y += self._dir[1]

    def draw(self, screen: pygame.Surface, tile_size: int, color: tuple) -> None:
        """Draws the ant with an arrow pointing in its direction."""
        # Calculate the center of the tile where the ant is located
        center_x = self._x*tile_size + tile_size//2
        center_y = self._y*tile_size + tile_size//2
        half_size = tile_size//4
        
        # Determine the triangle vertices based on direction
        if self._dir == Dir.UP:
            points = [
                (center_x, center_y - half_size),
                (center_x - half_size, center_y + half_size),
                (center_x + half_size, center_y + half_size)
            ]
        elif self._dir == Dir.RIGHT:
            points = [
                (center_x + half_size, center_y),
                (center_x - half_size, center_y - half_size),
                (center_x - half_size, center_y + half_size)
            ]
        elif self._dir == Dir.DOWN:
            points = [
                (center_x, center_y + half_size),
                (center_x - half_size, center_y - half_size),
                (center_x + half_size, center_y - half_size)
            ]
        elif self._dir == Dir.LEFT:
            points = [
                (center_x - half_size, center_y),
                (center_x + half_size, center_y - half_size),
                (center_x + half_size, center_y + half_size)
            ]

        pygame.draw.polygon(screen, color, points)

    @classmethod
    def create(cls, board: Board) -> typing.Self:
        """Creates an ant directed UP and places it randomly on the board."""

        # Chooses the beginning tile
        random.seed()
        x = board.nb_cols//2
        y = 0, board.nb_lines//2

        return cls(x, y, direction = Dir.UP)