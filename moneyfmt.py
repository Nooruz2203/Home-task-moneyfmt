import moneyfmt

class MoneyFmt:
    def __init__(self, value): 
        self.value = value
    def __str__(self):
        if self.value >= 0:
            return '${:,.2f}'.format(self.value)
        else:
            return '-${:,.2f}'.format(-self.value)
    def update(self, value=None):
        self.value=value
    def repr(self):
        print(self.value)
        return f'{self.value}'

cash = moneyfmt.MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
repr(cash)
print(cash)