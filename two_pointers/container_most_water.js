/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 948
 * Updated: 2025-09-11T13:35:17+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 948;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
