/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 718
 * Updated: 2025-07-14T20:53:04+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 718;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
