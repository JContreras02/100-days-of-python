student_scores = [2, 4, 5, 27, 2333, 37, 2, 1, 24, 522, 26, 3, 76, 83, 9]

def find_max_num(list):

    max_score = 0

    for i in list:
       if max_score < i:
           max_score = i
    print(max_score)

find_max_num(student_scores)