class Bankkonto:
    def __init__(self, namn, saldo):
        self.__saldo = saldo
        self.namn = namn

    def get_saldo(self):
        return self.__saldo

    def sätt_in_pengar(self, insättning):
        self.__saldo += insättning

    def ta_ut_pengar(self, uttag):
        if uttag <= self.__saldo:
            self.__saldo -= uttag
        else:
            print("Du har inte tillräckligt med pengar.")

bankkonto = Bankkonto("Emil", 1000)

bankkonto.sätt_in_pengar(2000)

bankkonto.ta_ut_pengar(10000)

print(bankkonto.get_saldo())
