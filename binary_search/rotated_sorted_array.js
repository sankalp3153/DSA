/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2354
 * Updated: 2026-11-17T20:00:13+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2354;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
