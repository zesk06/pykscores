# pylint fail to discover some mongoengin members
# pylint: disable=E1101
import pykscores.database as db
from pykscores.database import User, Play, UserScore
import datetime
db.connect()


def test_user():
    # try to insert albert
    if User.objects(login='albert'):
        for user in User.objects(login='albert'):
            print('delete previous albert')
            user.delete()
    new_u = User(login='albert')
    new_u.save()
    print('saved new_user')


def test_play():
    new_p = Play()
    new_p.date = datetime.datetime.now()

    user1 = User.find_one(login='albert', create=True)
    user2 = User.find_one(login='gerard', create=True)

    score1 = UserScore(user=user1, score=10)

    score2 = UserScore(user=user2, score=100)

    new_p.scores = [score1, score2]
    new_p.save()
