import itertools

for answer in itertools.product('ABCD', repeat=10):
    ans = ['0']
    ans.extend(answer)

    # question 2
    if (ans[2] == 'A' and ans[5] != 'C') \
            or (ans[2] == 'B' and ans[5] != 'D') \
            or (ans[2] == 'C' and ans[5] != 'A') \
            or (ans[2] == 'D' and ans[5] != 'B'):
        continue

    # question 3
    if (ans[3] == 'A' and ans[3] in [ans[6], ans[2], ans[4]]) \
            or (ans[3] == 'B' and ans[6] in [ans[3], ans[2], ans[4]]) \
            or (ans[3] == 'C' and ans[2] in [ans[6], ans[3], ans[4]]) \
            or (ans[3] == 'D' and ans[4] in [ans[6], ans[2], ans[3]]):
        continue

    # question 4
    if (ans[4] == 'A' and ans[1] != ans[5]) \
            or (ans[4] == 'B' and ans[2] != ans[7]) \
            or (ans[4] == 'C' and ans[1] != ans[9]) \
            or (ans[4] == 'D' and ans[6] != ans[10]):
        continue

    # question 5
    if (ans[5] == 'A' and ans[8] != ans[5]) \
            or (ans[5] == 'B' and ans[4] != ans[5]) \
            or (ans[5] == 'C' and ans[9] != ans[5]) \
            or (ans[5] == 'D' and ans[7] != ans[5]):
        continue

    # question 6
    if (ans[6] == 'A' and len({ans[2], ans[4], ans[8]}) != 1) \
            or (ans[6] == 'B' and len({ans[1], ans[6], ans[8]}) != 1) \
            or (ans[6] == 'C' and len({ans[3], ans[10], ans[8]}) != 1) \
            or (ans[6] == 'D' and len({ans[5], ans[9], ans[8]}) != 1):
        continue

    # question 7
    choose_freq = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for item in ans[1:]:
        choose_freq[item] += 1
    sorted_choose_freq = sorted(choose_freq.items(), key=lambda d: d[1])
    if sorted_choose_freq[0][1] == sorted_choose_freq[1][1]:
        continue
    min_item = sorted_choose_freq[0][0]

    if (ans[7] == 'A' and min_item != 'C') \
            or (ans[7] == 'B' and min_item != 'B') \
            or (ans[7] == 'C' and min_item != 'A') \
            or (ans[7] == 'D' and min_item != 'D'):
        continue

    # question 8
    if (ans[7] == 'A' and abs(ord(ans[7]) - ord(ans[1])) != 1) \
            or (ans[7] == 'B' and abs(ord(ans[5]) - ord(ans[1])) != 1) \
            or (ans[7] == 'C' and abs(ord(ans[2]) - ord(ans[1])) != 1) \
            or (ans[7] == 'D' and abs(ord(ans[10]) - ord(ans[1])) != 1):
        continue

    # question 9
    if (ans[9] == 'A' and (ans[1] == ans[6] and ans[6] == ans[5])) \
            or (ans[9] == 'B' and (ans[1] == ans[6] and ans[10] == ans[5])) \
            or (ans[9] == 'C' and (ans[1] == ans[6] and ans[2] == ans[5])) \
            or (ans[9] == 'D' and (ans[1] == ans[6] and ans[9] == ans[5])):
        continue

    # question 10
    diff_between_max_min_freq = sorted_choose_freq[3][1] - sorted_choose_freq[0][1]
    if (ans[10] == 'A' and diff_between_max_min_freq != 3) \
            or (ans[10] == 'B' and diff_between_max_min_freq != 2) \
            or (ans[10] == 'C' and diff_between_max_min_freq != 4) \
            or (ans[10] == 'D' and diff_between_max_min_freq != 1):
        continue

    print(ans[1:])
