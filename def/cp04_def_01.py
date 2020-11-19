def solution(S):
    # write your code in Python 3.6
    n = 0
    balloon = 'BALLOON'
    index = 0
    while len(S) > 0:
        if balloon[index] in S:
            S = S.replace(balloon[index], '', 1)
        else:
            break
        index += 1
        if index == len(balloon):
            n += 1
            index = 0

    return n


if __name__ == "__main__":
    case1 = 'BAONXXOLL'
    case2 = 'BAOOLLNNOLOLGBAX'
    print('Word (BALLOON) appear {} times in ({})'.format(solution(case1), case1))
    print('Word (BALLOON) appear {} times in ({})'.format(solution(case2), case2))
