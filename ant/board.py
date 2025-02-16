# à faire : fonctions pour : de quelle couleur est la tile x, y
# faire défiler défiler board
# draw
# output

import pygame

from .tile import Tile
from .ant import Ant
from .dir import Dir

WHITE = (255, 255, 255)

class Board:
    """The board."""

    def __init__(self, screen: pygame.Surface, nb_lines: int, nb_cols: int,
                 tile_size: int) -> None:
        self._screen = screen
        self._nb_lines = nb_lines
        self._nb_cols = nb_cols
        self._tile_size = tile_size
        self._tiles = [[Tile(x, y, WHITE) for x in range(self._nb_cols)] for y in range(self._nb_lines)]

    @property
    def nb_lines(self):
        """Gives how many lines the board counts."""
        return self._nb_lines
    
    @property
    def nb_cols(self):
        """Gives how many columns the board counts."""
        return self._nb_cols
    
    def get_tile(self, x: int, y: int) -> Tile:
        """Gives the tile at given coordinates."""
        return self._tiles[y][x]

    def draw_board(self, ant: Ant, color: tuple) -> None:
        for tile in self._tiles:
            tile.draw(self._screen, self._tile_size)
        ant.draw(self._screen, self._tile_size, color)

    def output(self, final_states: list[dict], ant: Ant, step: int) -> list[dict]:
        """Create the output including the step, coordinates x and y of the ant, its direction and the schema."""
        directions = {Dir.UP: "UP", Dir.DOWN: "DOWN", Dir.LEFT: "LEFT", Dir.RIGHT:"RIGHT"}
        # Drawing the final state
        schema = ["" for y in range(self._nb_lines)]
        for y in range(self._nb_lines):
            for tile in self._tiles[y]:
                if tile.color == WHITE:
                    schema[y] += " "
                else:
                    schema[y] += "X"

        final_states.append({"step": step, "x": ant.x, "y": ant.y, "direction": directions[ant.dir], "schema": schema})

        # Prints the final state
        print(f"Step : {step}")
        print(f"{ant.x}, {ant.y}, {directions[ant.dir]}")
        print("\n".join(schema))

        return final_states