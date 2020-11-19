S = 'BAONXXOLL'
n = 0
balloon = 'BALLOON'
index = 0

while len(S) > 0:  # = len(balloon):
    if balloon[index] in S:
        S = S.replace(balloon[index], '', 1)
    else:
        break
    index += 1
    if index == len(balloon):
        n += 1
        index = 0

print('Word ({}) appear {} times in (BAONXXOLL)'.format(balloon, n))
