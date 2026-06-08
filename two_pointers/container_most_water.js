/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1845
 * Updated: 2026-06-08T17:31:52+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1845;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
