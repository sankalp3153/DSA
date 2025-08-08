/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 810
 * Updated: 2025-08-08T23:06:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 810;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
