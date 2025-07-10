import art
print(art.logo)
print("Welcome to the secret auction! \n")

# Function to help find the highest bidder
def find_highest_bidder(bidding_dictionary):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}!")

# Setting loop to true then later setting it to false when done
program = True

# Empty dictionary to store keys and values
bids = {}

# While loop that will continue asking for names and bids until user says no
while program is True:

    name = input("What is your name?: ")
    try:
        price = int(input("What is your bid?: $"))
    except ValueError:
        print("Did not recognize input. Bidding has ended.")
        break

    bids[name] = price

    #if statement to decide if there are more bidders or not 
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no':  \n").lower()
    if other_bidders == "yes":
        print("\n" * 50)
        print(art.logo)

    elif other_bidders == "no":
        program = False
        find_highest_bidder(bids)
    else:
        print("Invalid input. Ending bidding.")
        program = False
        find_highest_bidder(bids)