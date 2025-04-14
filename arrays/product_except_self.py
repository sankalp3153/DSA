"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 415
Updated: 2025-04-14T12:21:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 415
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
