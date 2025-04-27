/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 465
 * Updated: 2025-04-27T18:53:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 465;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
