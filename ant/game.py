# Third party
import pygame
import yaml
from pathlib import Path

# First-party
from .ant import Ant
from .board import Board

class Game:
    """The main class of the game."""

    def __init__(self, nb_steps: int, tile_size: int, # noqa: PLR0913
                 fps: int,
                 ant_color: tuple,
                 final_file: Path,
                 gui: bool,
                 logger_obj,
                 nb_cols: int, nb_lines: int,
                 ) -> None:
        """Object initialization."""
        # Given arguments
        self._tile_size = tile_size
        self._fps = fps
        self._ant_color = ant_color
        self._final_file = final_file
        self._nb_steps = nb_steps
        self._gui = gui
        self._logger = logger_obj
        self._nb_cols = nb_cols
        self._nb_lines = nb_lines
        

    def _init(self):
        # Create the clock
        self._clock = pygame.time.Clock()

        # Screen creation
        screen_size = (self._nb_cols*self._tile_size,
                       self._nb_lines*self._tile_size)
        self._screen = pygame.display.set_mode(screen_size)
        self._logger.info("Screen created and drawn.")

        # Create the board and ant
        self._board = Board(self._screen, self._nb_lines, self._nb_cols, self._tile_size)
        self._logger.info("Board created.")
        self._ant = Ant.create(self._nb_lines, self._nb_cols)
        self._logger.info("Ant created.")

        # Checks if the final output file exists...
        if self._final_file.exists():
            with open(self._final_file, 'r') as f:
                final_states = yaml.safe_load(f)
            self._final_states = final_states
            self._logger.info("The output file was successfully readed.")
        # ...and if not, creates it
        else:
            self._final_states = []
            with self._final_file.open("w") as fd:
                yaml.safe_dump(self._final_states, fd)
            self._logger.info("The output file was successfully created.")

    def start(self) -> None:
        """Start the game."""
        self._logger.info("Game started.")
        
        if self._gui:
            # Initialize pygame
            pygame.init()

        # Initialize game
        self._init()
        i = 0
        flag = True

        # Start pygame loop
        while i < self._nb_steps and flag:

            if self._gui:
                self._logger.debug("GUI mode is on.")
                # Wait 1/FPS second
                self._clock.tick(self._fps)

            # Check for quit : closing window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                    self._logger.info("Exited the game.")
                # Key press
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_q:
                            flag = False
                            self._logger.info("Exited the game.")

            # Update object
            tile = self._board.get_tile(self._ant.x, self._ant.y)
            self._logger.debug("The tile where the ant is currently on was gotten back.")
            self._board.move(tile, self._ant)
            self._logger.info("Ant moved.")

            # Display
            if self._gui:
                # Caption title bar
                pygame.display.set_caption(f"Langton's Ant - Step {i}")
                # Draw board and ant
                self._board.draw_board(self._ant, self._ant_color)
                self._logger.info("Board drawn.")
                pygame.display.update()

            # Increase number of steps
            i += 1
        
        # Updates output file and prints the result of the final state
        self._final_states = self._board.output(self._final_states, self._ant, i)
        with open(self._final_file, 'w') as f:
            yaml.safe_dump(self._final_states, f)
        self._logger.info("Final state included in the yml file.")
        
        if self._gui:
            # Terminate pygame
            pygame.quit()