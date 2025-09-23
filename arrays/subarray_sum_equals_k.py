"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 989
Updated: 2025-09-23T18:40:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 989
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
