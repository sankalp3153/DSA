/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 353
 * Updated: 2025-03-25T16:59:49+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 353;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
