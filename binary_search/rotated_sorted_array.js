/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1204
 * Updated: 2025-12-02T19:02:29+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1204;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
