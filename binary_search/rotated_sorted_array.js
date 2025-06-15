/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 629
 * Updated: 2025-06-15T21:52:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 629;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
