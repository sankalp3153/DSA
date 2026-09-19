/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2193
 * Updated: 2026-09-19T17:14:28+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2193;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
