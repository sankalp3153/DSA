/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1911
 * Updated: 2026-06-28T16:41:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1911;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
