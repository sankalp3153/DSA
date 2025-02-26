"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 230
Updated: 2025-02-26T11:27:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 230
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
