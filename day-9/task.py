import art

print(art.logo)

is_bidding = True
bids = {}

while is_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        is_bidding = False

    print("\n" * 100)

winner = max(bids, key=bids.get)

print(f"The winner is {winner} with a bid of ${bids[winner]}")
