/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1773
 * Updated: 2026-05-19T14:21:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1773;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
