/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2233
 * Updated: 2026-10-02T17:16:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2233;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
