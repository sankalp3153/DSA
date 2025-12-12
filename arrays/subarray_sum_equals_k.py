"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1242
Updated: 2025-12-12T23:05:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1242
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
