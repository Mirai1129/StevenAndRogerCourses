def buy_fruit(money):
    if money >= 100:
        fruit = "apple"
    else:
        fruit = "banana"
    return fruit

def buy_drugs(blablabla):
    if blablabla >= 100:
        drug = "cocaine"
        return drug
    else:
        return "no drug"

# practice without return statement
BANK = 0
def save_money(money):
    BANK += money


def go_to_nice_work():
    salary = 1000
    return salary

def go_to_bad_work():
    salary = 1000

class People:
    def __init__(self, name):
        self.name = name
        
    def eat(self, food = None):
        print(f"{self.name} eat {food}")

Roger = People("Roger")
Steven = People("Steven")

Roger.eat("apple")
Steven.eat("banana")
Roger.eat()

def play(stuff):
    print(f"Playing with {stuff}")
    
play("soccer")
play("basketball")
play("tennis")
