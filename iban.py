import random

def IBAN():
    nummers = "".join(str(random.randint(0, 9)) for _ in range(2))
    letters = "".join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4))
    rekeningnummer = "".join(str(random.randint(0, 9)) for _ in range(10))
    bankrekeningnummer = "NL{}{}{}".format(nummers,letters,rekeningnummer)
    return bankrekeningnummer