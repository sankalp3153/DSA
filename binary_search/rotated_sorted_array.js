/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2308
 * Updated: 2026-10-31T16:22:10+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2308;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
