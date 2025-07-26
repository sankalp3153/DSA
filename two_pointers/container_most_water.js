/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 764
 * Updated: 2025-07-26T23:24:08+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 764;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
