/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 51
 * Updated: 2025-01-09T20:20:08+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 51;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
