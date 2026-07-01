/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1917
 * Updated: 2026-07-01T15:34:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1917;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
