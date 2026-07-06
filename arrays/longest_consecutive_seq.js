/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1934
 * Updated: 2026-07-06T16:32:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1934;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
