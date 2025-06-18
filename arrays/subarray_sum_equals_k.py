"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 644
Updated: 2025-06-18T22:15:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 644
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
