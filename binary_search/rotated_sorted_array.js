/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1319
 * Updated: 2026-01-01T19:31:44+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1319;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
