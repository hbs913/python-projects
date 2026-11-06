def split_bill(total, tip_percent, people):
    tip=total*(1+(tip_percent/100))
    amount=(tip/people)
    return amount
total = float(input("Bill total: "))
tip_percent = float (input("Tip percent: "))
people = int(input("How many people:"))
share = split_bill(total, tip_percent, people)
print(f" Each person pays ${share:.2f}")