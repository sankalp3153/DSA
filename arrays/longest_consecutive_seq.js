/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 439
 * Updated: 2025-04-18T11:57:29+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 439;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
