import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Calculator:
    description: str = "Simple calculations: +.-,*,/"

    def __init__(self, number_one: str, number_two: str):
        self.number_one = number_one
        self.number_two =number_two

    def add(self):
        return self.number_one + self.number_two
    
    def div(self):
        return self.number_one - self.number_two
    
    def multi(self):
        return self.number_one * self.number_two
    
    def sub(self):
        return self.number_one / self.number_two
    
if __name__ == "__main__":
    number_one = int(input("Please enter first number: "))
    number_two = int(input("Please enter second number: "))   
    
    calcu = Calculator(number_one, number_two)
    print(f"Addition: {calcu.add()}\nDivision: {calcu.div()}\nMultiplication: {calcu.sub()}\nSubstraction: {calcu.sub()}")
