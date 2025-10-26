/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1086
 * Updated: 2025-10-26T14:43:41+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1086;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
