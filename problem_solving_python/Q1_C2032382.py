import csv
import random
import matplotlib.pyplot as plt
random.seed(57)

#(A)


def game(ra, rb):
    p = ra/(ra + rb)
    p_1 = 0
    p_2 = 0
    while (p_1 < 11 and p_2 < 11) or (p_1 - p_2 < 2) and (p_2 - p_1 < 2):
        r = random.random()
        if r < p:
            p_1 += 1
        else:
            p_2 += 1
    return p_1, p_2


print(game(70, 30))



#(B)


def winProbability(ra, rb, n):
    p_A_Wins = 0
    p_B_Wins = 0
    for i in range(n):
        p_A_score, p_B_score = game(ra, rb)
        if p_A_score > p_B_score:
            p_A_Wins += 1
        else:
            p_B_Wins += 1

    Probability_PlayerA_Wins = p_A_Wins/(p_A_Wins + p_B_Wins)
    return(Probability_PlayerA_Wins)


print(winProbability(70, 30, 10000))




#(C)


def abilities():
    with open('abilities.csv', newline='') as csv_file:
        rdr = csv.reader(csv_file)
        list = []
        for row in rdr:
            tuple = (int(row[0]), int(row[1]))
            list.append(tuple)
        return(list)


print(abilities())



#(D)



def graph():
    r = []
    prob = []
    for i in abilities():
        ra = i[0]
        rb = i[1]
        n = 10000
        winProbability(ra, rb, n)
        blah = i[0]/i[1]
        r.append(blah)
        prob.append(winProbability(ra, rb, n))
    plt.plot(r, prob)
    plt.xlabel('Ra/Rb')
    plt.ylabel('Probability')
    plt.show()


print(graph())



#(e)


def match(ra, rb, n):
    blah = [0, 0]
    while True:
        result = game(ra, rb)
        if result[0] > result[1]:
            blah[0] += 1
        else:
            blah[1] += 1
        if(blah[0] >= n):
            return "a"
        elif(blah[1] >= n):
            return "b"

#print(matches(50, 50, 1000))

def matches(ra, rb, n, mn = 10000):
    counter = [0, 0]
    for i in range(mn):
        blah = match(ra, rb, n)
        if blah == "a":
            counter[0] += 1
        elif blah == "b":
            counter[1] += 1
    print(counter[0])
    print(counter[1])
    WinProb = float(counter[0]) / (float(counter[0]) + float(counter[1]))
    return WinProb


#print(matches(50, 50, 100,))

for i in range(1, 10):
    z = matches(60, 40, i)
    if z > 0.9:
        print(f"" + str(i), "games, probability", z)