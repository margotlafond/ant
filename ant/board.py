# Third party
import pygame

# First party
from .tile import Tile
from .ant import Ant
from .dir import Dir

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (193, 225, 255)

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
        """Draws the board."""
        for list in self._tiles:
            for tile in list:
                tile.draw(self._screen, self._tile_size)
        ant.draw(self._screen, self._tile_size, color)

    def output(self, final_states: list[dict], ant: Ant, step: int) -> list[dict]:
        """Create the output including the step, coordinates x and y of the ant, its direction and the schema."""
        directions = {Dir.UP: "UP", Dir.DOWN: "DOWN", Dir.LEFT: "LEFT", Dir.RIGHT:"RIGHT"}
        # Drawing the final state
        schema = ["" for y in range(self._nb_lines)]
        for y in range(self._nb_lines):
            for tile in self._tiles[y]:
                if tile.color == BLACK:
                    schema[y] += "X"
                else:
                    schema[y] += " "
        # Prints the final state
        print(f"Step : {step}")
        print(f"{ant.x}, {ant.y}, {directions[ant.dir]}")
        print("\n".join(schema))

        final_states.append({"step": step, "x": ant.x, "y": ant.y, "direction": directions[ant.dir], "schema": schema})

        return final_states
    
    def move(self, tile: Tile, ant: Ant) -> None:
        """
        Moves the ant : first checks the tile color, then turns, then changes the tile color, and then moves.
        Also grows the board if the ant is about to leave it.
        A blue tile means that the tile is white but has been visited.
        """
        # Changes the color and direction
        if tile.color == BLACK:
            ant.turn_left()
            tile.color = BLUE # This tile is white but has been visited
        else:
            ant.turn_right()
            tile.color = BLACK

        # Moves the ant
        ant.x += ant.dir.value[0]
        ant.y += ant.dir.value[1]

        # If the ant goes x < 0:
        if ant.x < 0:
            ant.x = 0
            for j in range(self._nb_lines):
                self._tiles[j].insert(0, Tile(0, j, WHITE))
                for i in range(1, self._nb_cols): #Modifies the x of the tiles because we inserted one at the beginning of the list
                    self._tiles[j][i].x = i
            self._nb_cols += 1

        # Ant goes x > nb of columns
        elif ant.x >= self._nb_cols:
            ant.x = self._nb_cols
            for j in range(self._nb_lines):
                self._tiles[j].append(Tile(self._nb_cols, j, WHITE))
            self._nb_cols += 1

        # Ant goes y < 0
        if ant.y < 0:
            ant.y = 0
            self._tiles.insert(0, [Tile(i, 0, WHITE) for i in range(self._nb_cols)])
            for j in range(1, self._nb_lines):
                for i in range(1, self._nb_cols): #Modifies the y of the tiles because we inserted a list of tiles at the beginning of the list
                    self._tiles[j][i].y = i
            self._nb_lines += 1

        # Ant goes y > nb of lines
        elif ant.y >= self._nb_lines:
            ant.y = self._nb_lines
            for j in range(self._nb_lines):
                self._tiles.append([Tile(i, self._nb_lines, WHITE) for i in range(self._nb_cols)])
            self._nb_lines += 1