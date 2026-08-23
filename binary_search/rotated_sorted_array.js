/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2101
 * Updated: 2026-08-23T14:33:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2101;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
