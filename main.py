# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# PART 1
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'

goal_0  =32 
goal_1  =54

scorers=\
    player1 +' ' + str(goal_0)+', '+\
    player2 +' ' + str(goal_1)
print(scorers)

report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'
print(report)

#PART 2
player      ='Ruud Gullit'
index_space =player.find(' ')
print(player.find(' '))

first_name  =player[:index_space]
last_name   =player[index_space+1:]
name_short  =f'{first_name[0]}. {last_name}'
print(name_short)

last_name_len   =len(last_name)
len_first_name  =len(first_name)

first_name_exclamation= first_name + '! '
chant=first_name_exclamation*len_first_name
chant=chant[:-1]
good_chant=(' ' != chant[-1])
print(chant)
print(good_chant)