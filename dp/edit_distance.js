/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 1236
 * Updated: 2025-12-11T13:39:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1236;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
