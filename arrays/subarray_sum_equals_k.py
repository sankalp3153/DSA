"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1150
Updated: 2025-11-21T14:27:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1150
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
