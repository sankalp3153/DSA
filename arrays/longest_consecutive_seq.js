/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 761
 * Updated: 2025-07-26T14:07:38+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 761;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
