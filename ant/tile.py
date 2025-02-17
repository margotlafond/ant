# Third party
import pygame

class Tile:
    """A square tile in the game. Includes a color."""
    
    def __init__(self, x: int, y: int, color: tuple) -> None:
        """Object initialization."""
        self._x = x # Column index
        self._y = y # Line index
        self._color = color

    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the tile."""
        return self._x
    
    @x.setter
    def x(self, new_x: int) -> None:
        """Set the new x."""
        self._x = new_x

    @property
    def y(self) -> int:
        """The y coordinate (i.e.: line index) of the tile."""
        return self._y
    
    @y.setter
    def y(self, new_y: int) -> None:
        """Set the new y."""
        self._y = new_y

    @property
    def color(self) -> tuple:
        """The color of the tile."""
        return self._color
    
    @color.setter
    def color(self, color: tuple) -> None:
        """Change the color of the tile."""
        self._color = color

    def draw(self, screen: pygame.Surface, size: int) -> None:
        """Draw the tile on screen."""
        rect = pygame.Rect(self.x*size, self.y*size, size, size)
        pygame.draw.rect(screen, self.color, rect)