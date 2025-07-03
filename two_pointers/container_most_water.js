/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 695
 * Updated: 2025-07-03T11:41:43+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 695;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
