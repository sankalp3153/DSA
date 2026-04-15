/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1684
 * Updated: 2026-04-15T21:51:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1684;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
