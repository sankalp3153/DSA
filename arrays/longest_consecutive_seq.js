/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 968
 * Updated: 2025-09-18T23:17:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 968;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
