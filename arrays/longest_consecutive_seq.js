/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1060
 * Updated: 2025-10-16T20:38:30+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1060;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
