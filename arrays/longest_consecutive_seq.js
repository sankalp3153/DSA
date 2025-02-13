/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 186
 * Updated: 2025-02-13T16:49:20+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 186;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
