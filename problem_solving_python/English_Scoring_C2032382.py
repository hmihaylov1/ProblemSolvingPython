import random


#random.seed()


#def game(ra, rb):
  #  a = "Player A"
  #  b = "Player B"
  #  players = [a, b]

 #   server = random.choice(players)
#    print(server)

#   p_1 = 0
 #   p_2 = 0

 #   p_ability = ra/(ra + rb)
 #   random.seed()

  #  while p_1 < 9 and p_2 < 9:
 #       r = random.random()
  #      if r <= p_ability and server == a:
 #           p_1 += 1
  #      elif r <= p_ability and server == b:
 #           server = a
  #      if r <= p_ability and server == b:
  #          p_2 += 1
   #     elif r <= p_ability and server == a:
    #        server = b
         #   print(server)

   # print(p_1)
   # print(p_2)

def english_game(ra, rb):
    s_a = s_b = rally = 0
    maximum_score = 9
    over = False
    server = None

    ability = ra / (ra + rb)
    random.seed()

    while over == False:
        random_probability = random.random()

        if random_probability < ability:
            if server == 'a':
                s_a += 1
            else:
                server = 'a'
        else:
            if server == 'b':
                s_b += 1
            else:
                server = 'b'
        if s_a == 8 and s_b == 8:
            if random_probability < 0.5:
                ending_score = 10
        rally += 1
        reached_play_to = (s_a == maximum_score) or (s_b == maximum_score)
        if reached_play_to:
            over = True
    return s_a, s_b, rally


print(english_game(50, 50))




#def eng_game(ra, rb):
 #   a = 'Player 1'
 #   b = 'Player 2'
 #   players = [a, b]

 #   server = random.choice(players)
 #   print(server)

 #   p_1 = 0
 #   p_2 = 0

 #   player_ability = ra / (ra + rb)
 #   random.seed()

  #  while p_1 < 9 and p_2 < 9:
  #      r = random.random()
 #       print(r)
  #      if r <= player_ability and server == a:
  #          p_1 += 1
  #      elif r <= player_ability and server == b:
  #          server = a
   #         print(server)

  #      if r > player_ability and server == b:
   #         p_2 += 1
  #      elif r > player_ability and server == a:
   #         server = b
    #        print(server)

  #  print(p_1)
  #  print(p_2)


#eng_game(50, 50)


def english_win_probability(ra, rb, n):
    p_a = 0
    p_b = 0
    random.seed(57)
    for i in range(n):
        random.random()
        score = english_game(ra, rb)
        if score[0] > score[1]:
            p_a += 1
        else:
            p_b += 1
    total = p_a/(p_a + p_b)
    return total

print(english_win_probability(70, 30, 10000))