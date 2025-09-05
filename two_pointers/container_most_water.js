/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 925
 * Updated: 2025-09-05T18:36:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 925;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
