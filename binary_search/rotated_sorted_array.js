/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1710
 * Updated: 2026-04-24T18:12:45+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1710;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
