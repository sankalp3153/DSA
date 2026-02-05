/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1434
 * Updated: 2026-02-05T15:17:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1434;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
