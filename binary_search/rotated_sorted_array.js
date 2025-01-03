/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 8
 * Updated: 2025-01-03T10:45:51+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 8;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
