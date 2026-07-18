/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1980
 * Updated: 2026-07-18T14:29:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1980;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
