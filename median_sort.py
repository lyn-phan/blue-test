"""Write a function medianSort() that accepts one argument: an array. The elements of this array can be
either numbers or arrays of numbers. The function should return the initial array sorted by the numbers
or the median values of the arrays of numbers.
For example:
medianSort([3, [-2, 4, 9]]) --> [3, [-2, 4, 9]]
The median of [-2, 4, 9] is 4, so we should sort that array after the 3.

medianSort([[12, 9, 1, 25], 4]) --> [4, [12, 9, 1, 25]]
The median of [12, 9, 1, 25] is 10.5, and 10.5 is greater than 4.

medianSort([[2.4, 0.2, 9.8], 0, [-1], [-9, -4]]) --> [[-9, -4], [-1], 0, [2.4,
0.2, 9.8]]

The median of [2.4, 0.2, 9.8] is 2.4. The median of [-1] is -1. The median of [-9, -4] is -6.5.
Therefore, the sorted order of these medians is [-6.5, -1, 0, 2.4]"""


# init tracker for current median
# init tracker for dictionary of medians
# loop through array
# if element is a list, take the median by sorting the list, finding the middle item
# median is --> if list is odd,
#       if list is even, divide by 2 - 1
# add median to dictionary as key, and the original list as value
# return the keys sorted

def medianSort(arr):
    medians_dict = {}
    sorted_array = []

    for item in range(len(arr)):
        if isinstance(arr[item], list):
            subarray = arr[item]
            # find the median
            if len(subarray) % 2 != 0:
                # total number of values are odd
                # subtract 1 since indexing starts at 0
                m = int((len(subarray)+1)/2 - 1)
                median = subarray[m]
                medians_dict[median] = subarray
            else:
                m1 = int(len(subarray) / 2 - 1)
                m2 = int(len(subarray) / 2)
                median = (subarray[m1] + subarray[m2]) / 2
                medians_dict[median] = subarray
        elif isinstance(arr[item], int):
            medians_dict[arr[item]] = arr[item]

    for key in sorted(medians_dict):
        sorted_array.append(medians_dict[key])

    return sorted_array


# arr = [3, [-2, 4, 9]]
# arr = [[12, 9, 1, 25], 4]
# arr = ([[2.4, 0.2, 9.8], 0, [-1], [-9, -4]])
print(medianSort(arr))
