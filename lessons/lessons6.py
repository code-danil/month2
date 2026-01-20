class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Money object amount={self.amount}"

    # equal >> ==
    def __eq__(self, other):
        if self.amount != other.amount:
            return False
        else:
            return True
        # return self.amount == other.amount

    # gt greater than -> >
    # lt = less than -> <
    # gte = greater than or equal -> >=
    # lte = less than or equal -> <=

    def __gt__(self, other):
        if self.amount > other.amount:
            return True
        else:
            return False


money_igor = Money(100)
money_danil = Money(101)
print(money_igor)
print(money_danil == money_igor)