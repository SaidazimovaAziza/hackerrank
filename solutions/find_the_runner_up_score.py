def find_runner_up_score():
    number_of_scores = int(input())
    set_of_scores = set()
    scores = input().split(' ')
    for index in range(len(scores)):
        set_of_scores.add(int(scores[index]))

    list_of_scores = sorted(set_of_scores, reverse=True)
    return list_of_scores[1]


print(find_runner_up_score())
