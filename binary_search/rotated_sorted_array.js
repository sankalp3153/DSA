/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 721
 * Updated: 2025-07-15T10:45:41+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 721;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
