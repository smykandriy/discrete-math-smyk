def generate_partitions(elements):
    length = len(elements)
    block = [1] * (length + 1)
    forward = [True] * (length + 1)
    next_element = [0] * (length + 1)
    prev_element = [0] * (length + 1)

    def print_partition():
        partition = []
        used_blocks = set(block[1:])
        for i in range(1, length + 1):
            if i in used_blocks:
                subset = [str(elements[j - 1]) for j in range(1, length + 1) if block[j] == i]
                partition.append(''.join(subset))
        print('(' + ')('.join(partition) + ')')

    print_partition()
    j = length
    while j > 1:
        k = block[j]
        if forward[j]:
            if next_element[k] == 0:
                next_element[k] = j
                prev_element[j] = k
                next_element[j] = 0
            if next_element[k] > j:
                prev_element[j] = k
                next_element[j] = next_element[k]
                prev_element[next_element[j]] = j
                next_element[k] = j
            block[j] = next_element[k]
        else:
            block[j] = prev_element[k]
            if k == j:
                if next_element[k] == 0:
                    next_element[prev_element[k]] = 0
                else:
                    next_element[prev_element[k]] = next_element[k]
                    prev_element[next_element[k]] = prev_element[k]
        print_partition()
        j = length
        while j > 1 and ((forward[j] and (block[j] == j)) or (not forward[j] and (block[j] == 1))):
            forward[j] = not forward[j]
            j -= 1


n = int(input("Enter n: "))
elements_list = list(range(1, n + 1))
generate_partitions(elements_list)
