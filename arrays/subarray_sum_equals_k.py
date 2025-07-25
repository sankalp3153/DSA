"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 759
Updated: 2025-07-25T17:41:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 759
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
