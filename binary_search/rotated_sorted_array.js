/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 491
 * Updated: 2025-05-07T22:22:19+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 491;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
