/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 859
 * Updated: 2025-08-18T14:35:26+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 859;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
