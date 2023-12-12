from replit import clear

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the bid amount is ${highest_bid}")

    
while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your bid price: $"))
    bids[name] = price
    bidders = input("Are there any bidders: ('yes' or 'no')")
    if bidders == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif bidders == 'true':
        clear()



