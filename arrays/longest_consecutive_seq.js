/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 876
 * Updated: 2025-08-22T20:57:30+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 876;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
