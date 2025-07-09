import art
print(art.logo)

# TODO-1: Ask the user for input                        DONE   
# TODO-2: Save data into dictionary {name: price}       DONE
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


# Setting loop to true then later setting it to false when done
program = True

# Empty dictionary to store keys and values
bidding_dict = {}


# while loop that will continue asking for names and bids until user says no
while program is True:
    name = input("What is your name?: ")

    bid = int(input("What is your bid?: $"))
    bidding_dict[name] = bid

    program = False

print(bidding_dict)