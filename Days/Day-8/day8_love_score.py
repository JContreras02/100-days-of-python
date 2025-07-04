def calculate_love_score(name1, name2):
    word = (name1 + name2).lower()
    
    count_for_true = 0
    count_for_love = 0

    for letter in word:
        if letter in "true":
            count_for_true += 1
        if letter in "love":
            count_for_love += 1

    true = str(count_for_true)
    love = str(count_for_love)
    final_count = true + love
    
    print(final_count)

calculate_love_score("Angela Yu", "Jack Bauer")