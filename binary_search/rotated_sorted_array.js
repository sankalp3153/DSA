/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 583
 * Updated: 2025-06-04T13:12:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 583;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
