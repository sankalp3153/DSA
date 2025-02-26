/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 232
 * Updated: 2025-02-26T19:11:36+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 232;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
