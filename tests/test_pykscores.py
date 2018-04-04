
from pykscores.cli import main
from pykscores.pykscores import User


def test_main():
    main([])


def test_user():
    ross = User()
    assert ross.email is None
