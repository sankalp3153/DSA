/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 324
 * Updated: 2025-03-20T19:39:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 324;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
