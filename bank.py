class Bank:
    __balance = 1000

    def get_balance(self):
        return self.__balance

class API(Bank):
    def print_balance(self):
        return self.get_balance()

obj = API()
print(obj.get_balance())
print(obj.print_balance())
