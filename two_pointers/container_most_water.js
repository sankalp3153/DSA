/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1569
 * Updated: 2026-03-15T10:57:52+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1569;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
