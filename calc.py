from data import Data

currency = Data()

#this function takes user input and determines if it is
def validity(a, b):

    valid = False

    if a in currency.getNames() and b in currency.getNames() and a != b:
        valid = True
        return valid
    return valid

def directQuote(a, b, num):
    val_1 = int(currency.getTable().get(a))
    val_2 = int(currency.getTable().get(b))
    return num * (val_2/val_1)

def IndirectQuote(a, b, num):
    val_1 = int(currency.getTable().get(a))
    val_2 = int(currency.getTable().get(b))
    return num * (val_1/val_2)

def main():
    running = True

    while running:

        #ask user for input
        userInput1 = input("Enter domestic currency: ").upper()
        userInput2 = input("Enter foreign currency: ").upper()

        if validity(userInput1, userInput2):
            domestic, foreign = (userInput1, userInput2)

            amount = abs(int(input("Enter the amount: ")))
            directQuote(domestic, foreign, amount)
            running = False
        else:
            print("Invalid input(s). Try again")

    print(directQuote(domestic, foreign, amount))

main()
