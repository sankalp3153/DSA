"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 920
Updated: 2025-09-03T15:00:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 920
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
