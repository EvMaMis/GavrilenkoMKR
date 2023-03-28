import pytest

import main


@pytest.mark.parametrize("path", ["firstFile", "secondFile"])
def test_get_right_open(path):
    file = main.openFile(path)
    assert file.name == f"{path}.txt"


@pytest.mark.parametrize("path", ["af", "aasf"])
def test_get_wrong_open(path):
    with pytest.raises(Exception):
        main.openFile(path)


def test_get_massive():
    file = main.openFile("firstFile")
    anotherFile = main.openFile("firstFile")
    massive = main.getLinesMassive(anotherFile)
    i = 0
    for line in file.readlines():
        assert line == massive[i]
        i += 1
