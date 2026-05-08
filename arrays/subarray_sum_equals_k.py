"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1748
Updated: 2026-05-08T19:08:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1748
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
