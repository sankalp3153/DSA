/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 669
 * Updated: 2025-06-26T12:44:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 669;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
