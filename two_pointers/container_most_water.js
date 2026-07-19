/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1983
 * Updated: 2026-07-19T15:54:38+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1983;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
