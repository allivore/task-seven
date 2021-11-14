def merge(*lists):
    unsorted_merged_list = []
    for current in lists:
        unsorted_merged_list.extend(current)

    return sorted(unsorted_merged_list)
