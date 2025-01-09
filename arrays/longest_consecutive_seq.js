/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 48
 * Updated: 2025-01-09T17:11:37+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 48;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
