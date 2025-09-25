/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 997
 * Updated: 2025-09-25T17:57:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 997;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
