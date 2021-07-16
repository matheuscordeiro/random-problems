def bonAppetit(bill, k, b):
    total_to_pay = 0
    for key, value in enumerate(bill):
        if key != k:
            total_to_pay += value

    ana_pay = int(total_to_pay/2)
    if b > ana_pay:
        print(b-ana_pay)
    else:
        print("Bon Appetit") 