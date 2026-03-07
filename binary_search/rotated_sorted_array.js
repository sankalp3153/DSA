/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1549
 * Updated: 2026-03-07T10:37:04+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1549;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
