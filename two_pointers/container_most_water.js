/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 97
 * Updated: 2025-01-24T14:22:26+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 97;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
