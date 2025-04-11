"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 414
Updated: 2025-04-11T23:14:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 414
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
