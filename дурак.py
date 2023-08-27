import random

naila = "Naila"
djemil = "Cemil"
rasim = "Rasim"
tofiq = "Tofiq"

group = [naila,djemil,rasim,tofiq]

cards = [
  ["red","black"],
  ["♡", "♤", "♧", "◇"],
  [6,7,8,9,10,"B","D","K","T"]
  ]

used_cards = []

def give_random():
  color = random.choice(cards[0])
  figure = random.choice(cards[1])
  name = random.choice(cards[2])
  card = f"{color} {figure} {name}"
  if card not in used_cards:
    used_cards.append(card)
    return card
  else:
    return give_random()


#1.Everbody claims cards
playersCs = [] #Symbolize players cards
for player in group:
  playersCs.append([]) #Opens list in list(playersCs) for cards for every player
for player in range(0,len(group)):
  for i in range(6):
    playersCs[player].append(give_random()) #Gives a random card to everyone
for i in range(0,len(playersCs)):
  print(f"{group[i]}'s cards:")
  for j in playersCs[i]:
    print(j)
  print("\n")

#2.Kozr and other cards
kozr = give_random()
print(f"Kozr is {kozr}")
try:
  used_cards.remove(kozr)
except:
  print("Wrong!!!")
#for taking new card use give_random()

#3.Looking for small kozr and starter player
firstP_select = list(kozr)
def kozr6():
  firstP_select[-1] = "6"
  return ''.join(firstP_select)
def kozr7():
  firstP_select[-1] = "7"
  return ''.join(firstP_select)
def kozr8():
  firstP_select[-1] = "8"
  return ''.join(firstP_select)
def kozr9():
  firstP_select[-1] = "9"
  return ''.join(firstP_select)
def kozr10():
  firstP_select[-1] = "10"
  return ''.join(firstP_select)
def kozrB():
  firstP_select[-1] = "B"
  return ''.join(firstP_select)
def kozrD():
  firstP_select[-1] = "D"
  return ''.join(firstP_select)
def kozrK():
  firstP_select[-1] = "K"
  return ''.join(firstP_select)
def kozrT():
  firstP_select[-1] = "T"
  return ''.join(firstP_select)
recent_user = [0,0]
smallest_user = [20,0]
for i in range(0,len(playersCs)):
  if kozr6() in playersCs[i]:
    recent_user[0]=6
    recent_user[1]=i
  elif kozr7() in playersCs[i]:
    recent_user[0]=7
    recent_user[1]=i
  elif kozr8() in playersCs[i]:
    recent_user[0]=8
    recent_user[1]=i
  elif kozr9() in playersCs[i]:
    recent_user[0]=9
    recent_user[1]=i
  elif kozr10() in playersCs[i]:
    recent_user[0]=10
    recent_user[1]=i
  elif kozrB() in playersCs[i]:
    recent_user[0]=11
    recent_user[1]=i
  elif kozrD() in playersCs[i]:
    recent_user[0]=12
    recent_user[1]=i
  elif kozrK() in playersCs[i]:
    recent_user[0]=13
    recent_user[1]=i
  elif kozrT() in playersCs[i]:
    recent_user[0]=14
    recent_user[1]=i
  if smallest_user[0]>recent_user[0]:
    smallest_user[0]=recent_user[0]
    smallest_user[1]=recent_user[1]
print(f"{group[smallest_user[1]]} starts")

#4.Starter player puts a card for a player that is next to him/her from a custom list, yeni saat eqrebi istiqametinde deyil
player_turn = random.shuffle(group)

#Made by Tofiq