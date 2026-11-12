
def ask_number(prompt):
    

    while True:
        answer= input(prompt)
        try:
            price=float(answer)
            return price
            
            
        except ValueError:
            print("That's not a number, try again")

run=ask_number("How much was your meal?")
print (run)