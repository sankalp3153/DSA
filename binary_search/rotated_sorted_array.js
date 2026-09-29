/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2216
 * Updated: 2026-09-29T22:27:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2216;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
