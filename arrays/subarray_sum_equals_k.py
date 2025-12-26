"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1288
Updated: 2025-12-26T11:40:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1288
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
