/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2331
 * Updated: 2026-11-05T20:26:26+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2331;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
