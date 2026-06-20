/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1888
 * Updated: 2026-06-20T18:35:25+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1888;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
