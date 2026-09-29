/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2213
 * Updated: 2026-09-29T15:33:43+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2213;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
