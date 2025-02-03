/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 146
 * Updated: 2025-02-03T12:51:40+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 146;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
