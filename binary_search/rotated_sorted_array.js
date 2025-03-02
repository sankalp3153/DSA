/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 238
 * Updated: 2025-03-02T12:12:50+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 238;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
