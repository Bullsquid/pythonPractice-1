import random as r


def play_game():
    summ = 0
    for j in range(0, 4):
        summ += r.randint(1, 6)
    if summ < 9:
        return True
    else:
        return False


def experiment(n):
    success = 0
    for i in range(0, n):
        if play_game():
            success += 1
    p = success / float(n)
    return p


def gamble(start_capital, want_to_win):
    capital = start_capital
    i = 0
    while 0 < capital < capital+want_to_win:
        i += 1
        if play_game():
            capital += 10
        else:
            capital -= 1

    return {
        "capital": capital,
        "i": i
    }


p_win = experiment(1000)
print "Your chance to win is {}%".format(p_win*100)

initial_capital = input("Enter your initial capital: ")
target = input("Now enter the amount of money you would like to win: ")

answer = gamble(initial_capital, target)

if answer["capital"] > 0:
    print "Congratulations!",
else:
    print "Sorry!",
print "After {} plays you have {} cr.".format(answer["i"], answer["capital"])
