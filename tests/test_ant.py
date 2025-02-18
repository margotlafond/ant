import ant

def test_ant_creation() -> None:
    ant1 = ant.Ant(5, 4, ant.Dir.LEFT)
    assert ant1.x == 5
    assert ant1.y == 4
    assert ant1.dir == ant.Dir.LEFT

def test_ant_auto_creation() -> None:
    ant1 = ant.Ant.create(nb_cols=32, nb_lines=24)
    assert ant1.dir == ant.Dir.UP
    assert ant1.x == 16
    assert ant1.y == 12

def test_ant_setting_coord() -> None:
    ant1 = ant.Ant(1, 2, ant.Dir.DOWN)
    ant1.x = 3
    ant1.y = 7
    ant1.dir = ant.Dir.RIGHT
    assert ant1.x == 3
    assert ant1.y == 7
    assert ant1.dir == ant.Dir.RIGHT

def test_ant_turn() -> None:
    ant1 = ant.Ant(1, 2, ant.Dir.DOWN)
    ant1.turn_left()
    ant2 = ant.Ant(2, 2, ant.Dir.RIGHT)
    ant2.turn_right()
    ant3 = ant.Ant(3, 2, ant.Dir.UP)
    ant3.turn_right()
    ant4 = ant.Ant(3, 0, ant.Dir.UP)
    ant4.turn_left()
    assert ant1.dir == ant.Dir.RIGHT
    assert ant2.dir == ant.Dir.DOWN
    assert ant3.dir == ant.Dir.RIGHT
    assert ant4.dir == ant.Dir.LEFT

