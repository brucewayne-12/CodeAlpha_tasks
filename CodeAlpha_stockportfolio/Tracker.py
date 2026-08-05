stock_prices={"AAPL": 180, "TSLA":250 , "GOOG" : 140 , "AMZN" : 120, "MSFT" : 310}

portfolio = {}

while True :
    stock_name= input("Enter the stock symbol (or 'done' to finish): ")
    stock_name = stock_name.upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Sorry the stock isn't in stock price")
        continue

    try:
        quantity = int(input("Enter the quantity of " + stock_name + ":"))
        
    except ValueError :
        print("Value error!! write in numerical values")
        continue

    portfolio[stock_name] = portfolio.get(stock_name,0)+ quantity
    print(f"Added {quantity} shares of {stock_name}.\n")

total_investment = 0

for stock,qty in portfolio.items():
    price = stock_prices[stock]
    value= price * qty
    total_investment +=value
    print(f"{stock}: {qty} shares x ${price} =: ${value}")

print(f"\nTotal Investment value : ${total_investment}")


save_choice = input("\nWould you like to save this summary? (yes/no): ").lower().strip()

if save_choice == "yes":

    with open("portfolio_summary.txt", "w") as file:

        file.write("=== Portfolio Summary ===\n")

        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")

        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    
    print("Saved as portfolio_summary.txt")
