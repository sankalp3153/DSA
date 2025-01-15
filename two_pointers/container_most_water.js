/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 74
 * Updated: 2025-01-15T21:32:42+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 74;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
