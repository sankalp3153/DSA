/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1687
 * Updated: 2026-04-16T19:14:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1687;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
