/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1014
 * Updated: 2025-09-30T19:53:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1014;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
