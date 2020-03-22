"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

def moveZeroes_extracmemory(nums):
    """
    O(n)
    """
    outcome = []
    for i in nums:
        if i != 0:
            outcome.append(i)

    return outcome + [0]*(len(nums)-len(outcome))

def moveZeroes_inplace(nums):
    """
    O(n)
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]

    return nums


def test_moveZeroes_extracmemory():
    assert moveZeroes_extracmemory([0, 1, 0, 12, 3]) == [1, 12, 3, 0, 0]
    assert moveZeroes_extracmemory([0, 0, 0]) == [0, 0, 0]

def test_moveZeroes_inplace():
    assert moveZeroes_inplace([0, 1, 0, 12, 3]) == [1, 12, 3, 0, 0]
    assert moveZeroes_inplace([0, 0, 0]) == [0, 0, 0]

test_moveZeroes_extracmemory()
test_moveZeroes_inplace()
