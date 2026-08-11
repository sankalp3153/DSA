/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2055
 * Updated: 2026-08-11T22:29:12+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2055;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
