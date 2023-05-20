from itertools import combinations


def generate_subsets(set_size, subset_size):
    my_set = list(range(1, set_size + 1))
    subset_list = list(combinations(my_set, subset_size))
    return subset_list


my_set_size = 5
my_subset_size = 3
subsets = generate_subsets(my_set_size, my_subset_size)
for subset in subsets:
    print(subset)
