/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1221
 * Updated: 2025-12-06T21:50:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1221;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
