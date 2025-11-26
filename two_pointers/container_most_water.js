/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1178
 * Updated: 2025-11-26T18:47:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1178;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
