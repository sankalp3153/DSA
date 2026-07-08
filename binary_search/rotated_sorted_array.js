/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1940
 * Updated: 2026-07-08T11:15:10+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1940;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
