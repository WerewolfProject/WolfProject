from player import Player
from job_list import *

if __name__ == "__main__":

    player1 = Player("player1", Citizen())
    player2 = Player("player2", Wolf())
    player3 = Player("player3", Diviner())
    player1 = Player("player4", Citizen())
    player1 = Player("player5", Citizen())
    player1 = Player("player6", Citizen())

    player1.job.comingout()
    player2.job.comingout()
    player3.job.comingout()

    player2.job.kill(player1)

    player3.job.divine(player1)
