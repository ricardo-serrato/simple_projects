hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
# First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.

total_price = sum(price for price in prices)

# After your loop, create a variable called average_price that is the total_price divided by the number of prices.
# You can get the number of prices by using the len() function

average_price = total_price / len(prices)

# prince the value of average_price
print(f"Average Haircut Price: {average_price}")

# reduce the price by 5 dollar for each haircut

new_prices = [new_price-5 for new_price in prices]
print(new_prices)

# set total_revenue to 0
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print(f"Total Revenue: {total_revenue}")


# get daily average of total revenue
average_daily_revenue = total_revenue/7
print(average_daily_revenue)


cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)