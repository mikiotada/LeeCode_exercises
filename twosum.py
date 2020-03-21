"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def twosum_bruteforce(nums, target):
    """
    Brute force searching, creating all possible combination
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i != j) and (nums[i]+nums[j] == target):
                return [i,j]

def twosum_nestedsearch(nums, target):
    """
    O(n^2)
    """
    for idx_ori, num_ori in enumerate(nums):
        target_remain = target - num_ori
        for idx_remain, num_remain in enumerate(nums):
            if (idx_ori != idx_remain) and (num_remain == target_remain):
                return [idx_ori, idx_remain]


def twoSum_hashmmap(nums, target):
        """
        O(n)
        """
        dic = {}

        for idx, num in enumerate(nums):
            remain = target - num
            if remain in dic:
                return [dic[remain], idx]

            else:
                dic[num] = idx


def test_bruteforce():
    assert twosum_bruteforce([3,2,4], 6) == [1, 2]
    assert twosum_bruteforce([2,5,5,7], 10) == [1, 2]
    assert twosum_bruteforce([2,7,11,15], 9) == [0, 1]

def test_nestedsearch():
    assert twosum_nestedsearch([3,2,4], 6) == [1, 2]
    assert twosum_nestedsearch([2,5,5,7], 10) == [1, 2]
    assert twosum_nestedsearch([2,7,11,15], 9) == [0, 1]

def test_hashmmap():
    assert twoSum_hashmmap([3,2,4], 6) == [1, 2]
    assert twoSum_hashmmap([2,5,5,7], 10) == [1, 2]
    assert twoSum_hashmmap([2,7,11,15], 9) == [0, 1]

test_bruteforce()
test_nestedsearch()
test_hashmmap()
