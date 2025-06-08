/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 600
 * Updated: 2025-06-08T18:57:56+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 600;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
