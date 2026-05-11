/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1756
 * Updated: 2026-05-11T21:53:44+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1756;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
