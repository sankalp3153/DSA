/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 1052
 * Updated: 2025-10-14T14:19:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1052;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
