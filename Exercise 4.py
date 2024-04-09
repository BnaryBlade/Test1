def sort_strings_by_length(strings):
    ascending_sorted = sorted(strings, key=len)

    descending_sorted = sorted(strings, key=len, reverse=True)

    return ascending_sorted, descending_sorted
