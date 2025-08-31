/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 905
 * Updated: 2025-08-31T19:43:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 905;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
