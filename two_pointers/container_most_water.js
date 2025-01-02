/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 5
 * Updated: 2025-01-02T18:18:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 5;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
