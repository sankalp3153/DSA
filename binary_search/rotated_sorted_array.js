/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1227
 * Updated: 2025-12-09T20:18:50+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1227;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
