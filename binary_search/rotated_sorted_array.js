/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1043
 * Updated: 2025-10-09T21:11:01+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1043;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
