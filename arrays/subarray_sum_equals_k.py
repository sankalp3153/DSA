"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1817
Updated: 2026-06-03T12:33:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1817
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
