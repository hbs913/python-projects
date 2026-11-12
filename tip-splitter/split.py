



def collect_orders():
    people= int(input("How mant people? "))

    ledger={}
    for count in range(people):
        

        name = input("Name: ")
        ledger[name]=0
        while ledger[name]>=0:
            price = float(input(f"{name}'s item (0 when done)"))
            if price ==0:
                break

        return ledger
print(collect_orders)

