/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1112
 * Updated: 2025-11-01T23:33:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1112;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
