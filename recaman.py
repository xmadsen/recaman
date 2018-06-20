def get_recaman_seq(max_size=100):

    visited = {num: False for num in range(max_size**2)}
    visited[1] = True

    curr_num = 1

    seq = [curr_num]

    for num in range(2, max_size):
        if curr_num - num > 0 and not visited[curr_num - num]:
            curr_num -= num
        else:
            curr_num += num
        seq.append(curr_num)
        visited[curr_num] = True

    return seq
