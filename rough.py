
# try:
#      num_of_players = int(input("Enter the number of Players's: "))
#      if num_of_players in range(2,6):
#           name_of_players = {input(f"Enter the name of Player {i+1} :") : [] for i in range(0,num_of_players)}
#      else:
#           raise Exception("Atleast 2 or Atmost 5 Players are needed to play this game")     
# except:
#      print("Atleast 2 or Atmost 5 Players are needed to play this game")

# # print(name_of_players)

# try:
#      times = int(input("Enter the number of times per player will throw dice? :"))
     
# except:
#      print('enter something valid')


# # print(name_of_players[0])
# # print(name_of_players[1])


# # print(times)

# def player_entry(dict_name,names):
#      for name in names:
#           dice = random.randint(1,6)
#           return dict_name[name].append(dice)   

# def dice(times):
#      try:
#           for i in range(0, times):
#                names = list(name_of_players.keys())
#                for name in names:
#                     input(f"{name} turn, enter 'Y' :")
#                     dice = random.randint(1,6)
#                     print(f'{name} got :{dice}')
#                     name_of_players[name].append(dice);
#      except:
#           return f'Something is not right!!'     
# dice(times)


# # print(name_of_players)

# def winner(dict_of_palyer):
#      for key, value in dict_of_palyer.items():
#           print(f'{key} : {value} and total is {sum(value)}')
#           name_of_players[key] = sum(value);
#      # names = list(name_of_players.keys())
#      winn = max(list(dict_of_palyer.values()))
#      for key, value in name_of_players.items():
#           if winn == value:
#                print(f'Winner is {key}')


# winner(name_of_players)
