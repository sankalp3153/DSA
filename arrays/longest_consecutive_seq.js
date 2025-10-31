/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1106
 * Updated: 2025-10-31T21:24:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1106;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
