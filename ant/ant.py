# First party
from .dir import Dir

# Third party
import pygame
import typing

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)

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
        """Set the new direction."""
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
    
    @x.setter
    def x(self, new_x: int) -> None:
        """Set the new x."""
        self._x = new_x
    
    @property
    def y(self) -> int:
        """The y coordinate (i.e.: line index) of the ant."""
        return self._y
    
    @y.setter
    def y(self, new_y: int) -> None:
        """Set the new y."""
        self._y = new_y


    def draw(self, screen: pygame.Surface, tile_size: int, color: tuple) -> None:
        """Draws the ant with an arrow pointing in its direction."""
        # Calculate the center of the tile where the ant is
        center_x = self._x*tile_size + tile_size//2
        center_y = self._y*tile_size + tile_size//2
        half_size = tile_size//4
        
        # Determine the triangle direction
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
    def create(cls, nb_lines: int, nb_cols: int) -> typing.Self:
        """Creates an ant directed UP and places it on the middle of the board."""

        # Chooses the beginning tile (middle tile)
        x = nb_cols//2
        y = nb_lines//2

        return cls(x, y, direction = Dir.UP)