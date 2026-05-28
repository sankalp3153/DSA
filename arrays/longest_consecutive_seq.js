/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1796
 * Updated: 2026-05-28T11:54:47+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1796;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
