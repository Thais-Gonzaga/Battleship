from src.batalha_naval import battleship


def test_battleship():
    grid = [[0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0]]
    assert battleship(grid, 0, 4) is True
    assert battleship(grid, 1, 4) is True
    assert battleship(grid, 2, 3) is True
    assert battleship(grid, 1, 1) is False
    assert battleship(grid, 3, 4) is False
