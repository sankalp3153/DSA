/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 235
 * Updated: 2025-03-01T11:32:37+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 235;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
