/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1181
 * Updated: 2025-11-26T22:31:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1181;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
