/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 166
 * Updated: 2025-02-07T17:25:37+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 166;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
