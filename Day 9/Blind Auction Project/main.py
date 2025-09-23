# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print(logo)
data_input = {}
reroute = 'yes'
while reroute == 'yes':
    name = input("What is your name:")
    bid = int(input("What is your bid: $"))
    reroute = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    data_input[name] = bid
    if reroute == 'yes':
        print("\n" * 50)
    if reroute == 'no':
        winner = max(data_input, key=data_input.get)
        print(f"the winner is {winner} with a bid of {data_input[winner]}  ")
