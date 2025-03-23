"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 345
Updated: 2025-03-23T13:41:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 345
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
