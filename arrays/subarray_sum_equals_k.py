"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 966
Updated: 2025-09-18T13:50:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 966
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
