def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('Nitish'))
print(lexicographi_sort('quickbrown'))
