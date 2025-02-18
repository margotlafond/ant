import ant

def test_tile_creation() -> None:
    black = (0, 0, 0)
    assert ant.Tile(1, 2, black).x == 1
    assert ant.Tile(1, 2, black).y == 2
    assert ant.Tile(1, 2, black).color == black

def test_tile_setting_coord() -> None:
    black = (0, 0, 0)
    white = (255, 255, 255)
    tile = ant.Tile(1, 2, black)
    tile.x = 3
    tile.y = 5
    tile.color = white
    assert tile.x == 3
    assert tile.y == 5
    assert tile.color ==  white