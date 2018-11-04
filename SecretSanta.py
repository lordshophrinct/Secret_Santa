import random

class Secret:
    def __init__(self, _giver, _receiver):
        self.giver = _giver
        self.receiver = _receiver
    def getGiver(self):
        return self.giver
    def getReceiver(self):
        return self.receiver

def arrangeSecrets(givers):
    getters = []
    secrets = []
    for name in givers:
        getters.append(name)
    
    for name in givers:
        r = random.randint(0, len(getters) - 1)
        s = Secret(name, getters[r])
        secrets.append(s)
        getters.pop(r)

    return secrets

filename = "names.txt"
file = open(filename, "r", encoding='UTF-8')
givers = file.read()
file.close()
givers = givers.split("\n")
good = False
while(not good):
    good = True
    secrets = arrangeSecrets(givers)
    for secret in secrets:
        if secret.getGiver() == secret.getReceiver():
            good = False

for secret in secrets:
    print("%-12s is buying for %-12s" % (secret.getGiver(), secret.getReceiver()))