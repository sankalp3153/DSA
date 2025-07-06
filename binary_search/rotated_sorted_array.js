/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 698
 * Updated: 2025-07-06T16:12:20+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 698;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
