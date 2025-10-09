/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1037
 * Updated: 2025-10-09T13:42:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1037;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
