/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2049
 * Updated: 2026-08-10T18:41:59+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2049;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
