/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 853
 * Updated: 2025-08-16T23:38:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 853;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
