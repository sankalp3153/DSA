/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2164
 * Updated: 2026-09-09T12:57:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2164;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
