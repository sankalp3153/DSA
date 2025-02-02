/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 143
 * Updated: 2025-02-02T19:15:54+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 143;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
