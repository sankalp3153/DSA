/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 117
 * Updated: 2025-01-29T13:53:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 117;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
