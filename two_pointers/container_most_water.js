/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 649
 * Updated: 2025-06-19T15:45:04+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 649;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
