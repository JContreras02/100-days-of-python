import art
print(art.logo)

# TODO-1: Ask the user for input                        DONE   
# TODO-2: Save data into dictionary {name: price}       DONE
# TODO-3: Whether if new bids need to be added          DONE
# TODO-4: Compare bids in dictionary


# Setting loop to true then later setting it to false when done
program = True

# Empty dictionary to store keys and values
bidding_dict = {}
highest_bidder = [0]


# while loop that will continue asking for names and bids until user says no
while program is True:

    name = input("What is your name?: ")

    bid = int(input("What is your bid?: $"))
    bidding_dict[name] = bid

    #if statement to decide if there are more bidders or not 
    
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.  ").lower()
    if other_bidders == "yes":
        continue
    elif other_bidders == "no":
        # call function

        program = False
    else:
        print("Did not recognize input. Bidding has ended.")

print(bidding_dict)

# finish function
def find_highest_bidder():
    for key in bidding_dict[key]:
            if bidding_dict[key] >= highest_bidder[0]:
                highest_bidder[0] = bidding_dict[key]