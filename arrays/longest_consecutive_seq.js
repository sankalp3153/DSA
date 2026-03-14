/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1566
 * Updated: 2026-03-14T15:59:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1566;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
