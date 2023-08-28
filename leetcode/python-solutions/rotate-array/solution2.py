"""
second solve using reversing algorithm
also uses a modulo operation on k
to ensure we don't rotate nums entirely
when k > length of nums

coded in 8m 30s using original tests
"""
def reverse(array, start, end):
    while start < end:
        tmp = array[end]
        array[end] = array[start]
        array[start] = tmp

        start += 1
        end -= 1

    return array

def rotate(nums, k):
    k = k % len(nums)
    last_element = len(nums) - 1

    nums = reverse(nums, 0, last_element)
    nums = reverse(nums, 0, (k - 1))
    nums = reverse(nums, k, last_element)

    return nums
