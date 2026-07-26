/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2003
 * Updated: 2026-07-26T17:37:10+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2003;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
