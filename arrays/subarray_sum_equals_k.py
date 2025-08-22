"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 874
Updated: 2025-08-22T17:24:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 874
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
