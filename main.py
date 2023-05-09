# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line



scorer_0 = 'Sanchez Lila'
scorer_1 = 'Daniel Ray'
goal_0 = 5
goal_1 = 10

scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)
print(scorers)

report = scorer_0 + ' scored in the ' + str(goal_0) + 'th minute\n' + scorer_1 + ' scored in the ' + str(goal_1) + 'th minute'
print(report)

player = scorer_0
first_name = player[:player.find(' ')]
print(first_name)

last_name_len = len(player[-player.find(' '):])
print(last_name_len)

name_short = player[:player.find(' ')].upper()[:1] + '.' + player[player.find(' '):]
print(name_short)

chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')])).strip()
print(chant)

good_chant = chant[-1:] != ' '
print(good_chant)