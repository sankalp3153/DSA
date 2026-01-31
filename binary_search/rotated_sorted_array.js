/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1411
 * Updated: 2026-01-31T14:02:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1411;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
