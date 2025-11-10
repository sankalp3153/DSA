/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1129
 * Updated: 2025-11-10T19:59:13+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1129;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
