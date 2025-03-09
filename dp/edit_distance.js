/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 270
 * Updated: 2025-03-09T11:04:56+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 270;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
