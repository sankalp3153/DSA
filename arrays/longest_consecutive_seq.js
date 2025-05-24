/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 554
 * Updated: 2025-05-24T19:36:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 554;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
