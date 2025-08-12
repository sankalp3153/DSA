/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 830
 * Updated: 2025-08-12T13:38:24+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 830;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
