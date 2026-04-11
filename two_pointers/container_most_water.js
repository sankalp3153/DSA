/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1661
 * Updated: 2026-04-11T13:05:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1661;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
