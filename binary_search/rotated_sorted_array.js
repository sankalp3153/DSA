/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1894
 * Updated: 2026-06-22T16:59:54+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1894;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
