def generate_subsets(set_size, subset_size):
    subset_list = []
    my_set = list(range(1, subset_size + 1))

    while True:
        subset_list.append(my_set[:])

        if my_set[subset_size - 1] == set_size:
            p = subset_size - 1
        else:
            p = subset_size

        while p >= 1:
            my_set[p - 1] += 1

            if p < subset_size:
                for i in range(p + 1, subset_size + 1):
                    my_set[i - 1] = my_set[p - 1] + i - p

            subset_list.append(my_set[:])

            if my_set[subset_size - 1] == set_size:
                p = p - 1
            else:
                p = subset_size

        if my_set[0] == set_size - subset_size + 1:
            break

    return subset_list


my_set_size = 5
my_subset_size = 3
subsets = generate_subsets(my_set_size, my_subset_size)
for subset in subsets:
    print(subset)
