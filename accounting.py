MELON_COST = 1.00  # set price for melon, easier to update if needed


def get_customer_balance(filepath):
    """takes in raw customer receipt data from a file, generates a report to show how much a customer owes or has in balance 
    """
    data_summary = open(filepath)  # binding data_summary to a file content
    for line in data_summary:  # iterate each line in the file

        line = line.rstrip()
        words = line.split('|')
        customer = words[1]
        melon_quantity = int(words[2])
        payment = float(words[-1])
        amount_owed = melon_quantity * MELON_COST

        print(f"{customer} paid ${payment:.2f},",
              f"expected ${amount_owed:.2f}"
              )
        if amount_owed < payment:
            print(
                f"{customer} has ${round(payment - amount_owed, 2)} in credit ")
        elif amount_owed > payment:
            print(
                f"{customer} owes ${round(amount_owed - payment, 2)}. ")

    data_summary.close()


print(get_customer_balance('customer-orders.txt'))

# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
