



TAX_RATE = 0.08875   # NYC combined sales tax

def collect_orders():
    """Ask for each person's items; return {name: food_subtotal}."""
    people = int(input("How many people? "))
    ledger = {}
    for _ in range(people):
        name = input("Name: ")
        ledger[name] = 0
        while True:
            price = float(input(f"{name}'s item (0 when done): "))
            if price == 0:
                break
            ledger[name] += price
    return ledger

def compute_shares(ledger, tip_percent):
    """Return {name: total_owed}, tax and tip applied to each person's food."""
    multiplier = 1 + TAX_RATE + tip_percent / 100   # tip figured on pre-tax food
    shares = {}
    for name, subtotal in orders.items():
        shares[name] = subtotal * multiplier
    return shares
orders = collect_orders()
tip = float(input("Tip percent? "))
shares = compute_shares(orders, tip)
for name, owed in shares.items():
    print(f"{name}: ${owed:.2f}")
