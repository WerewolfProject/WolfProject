class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.isAlive = True

    def isDead(self):
        self.isAlive = False
        print '%s(%s) is dead now' % (self.name, self.job)

    def showPlayer(self):
        if self.isAlive:
            print '%s(%s) is alvie' % (self.name, self.job)
        if not self.isAlive:
            print '%s(%s) is dead' % (self.name, self.job)
