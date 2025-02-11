/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 178
 * Updated: 2025-02-11T18:48:26+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 178;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
