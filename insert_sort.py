def insertion_sort (unsorted):
    sorted = []
    
    for item in unsorted:
        i = 0
        for sorted_item in sorted:
            if item>sorted_item:
                i = i + 1
            else:
                break
        sorted.insert(i, item)
    return sorted

print(insertion_sort([1,2,5,64,74,435,63,6314,623,54,325,7]))