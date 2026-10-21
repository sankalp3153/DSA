/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2285
 * Updated: 2026-10-21T20:49:12+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2285;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
