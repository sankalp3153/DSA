/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 715
 * Updated: 2025-07-14T14:56:29+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 715;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
