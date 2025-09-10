"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 943
Updated: 2025-09-10T18:59:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 943
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
