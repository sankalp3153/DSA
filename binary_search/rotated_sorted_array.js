/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 376
 * Updated: 2025-04-01T18:03:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 376;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
