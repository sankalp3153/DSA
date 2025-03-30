/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 362
 * Updated: 2025-03-30T12:22:03+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 362;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
