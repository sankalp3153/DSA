/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1638
 * Updated: 2026-04-03T15:44:17+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1638;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
