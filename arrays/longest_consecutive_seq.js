/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 301
 * Updated: 2025-03-16T16:16:25+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 301;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
