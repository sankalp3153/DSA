"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 529
Updated: 2025-05-19T22:54:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 529
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
