# coding:utf-8


class Job:

    def __init__(self):
        self.name = ""

    def say(self, contents):
        print contents

    def comingout(self):
        self.say("私の職業は" + self.name + "です．")


class Diviner(Job):
    divinedResult = []

    def __init__(self):
        self.name = "占い師"

    def divine(self, player):
        self.divinedResult.append((player.name, player.job))

        if isinstance(player.job, Wolf):
            self.say(player.name + "さんは人狼です．")
        else:
            self.say(player.name + "さんは人間です．")


class Wolf(Job):

    def __init__(self):
        self.name = "人狼"

    def kill(self, player):
        player.isDead()


class Citizen(Job):

    def __init__(self):
        self.name = "市民"
