# Suppose you have $100, which you can invest with a 10% return each year. After one year, it's 100×1.1=110 dollars.
#  Add code to calculate how much money you end up with after 7 years, and print the result.

def invest(amount,year):
    intrest_rate = 10
    for i in range(year):
        amount = amount + (amount * intrest_rate / 100)
    print(amount)
amount = int(input("Enter Amount: "))
year = int(input("Enter Year: "))
invest(amount,year)
