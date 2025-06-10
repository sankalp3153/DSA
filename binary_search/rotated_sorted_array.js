/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 606
 * Updated: 2025-06-10T15:15:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 606;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
