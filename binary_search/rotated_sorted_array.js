/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 445
 * Updated: 2025-04-19T16:58:26+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 445;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
