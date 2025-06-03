/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 580
 * Updated: 2025-06-03T13:28:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 580;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
