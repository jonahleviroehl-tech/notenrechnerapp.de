(function (root) {
  'use strict';
  function number(value) {
    const text = String(value ?? '').trim();
    if (!/^[+-]?(?:\d+(?:[.,]\d*)?|[.,]\d+)$/.test(text)) return null;
    const result = Number(text.replace(',', '.'));
    return Number.isFinite(result) ? result : null;
  }
  function weightedAverage(rows, minimum, maximum) {
    let sum = 0, weights = 0, count = 0;
    for (const row of rows) {
      if (String(row.value).trim() === '') continue;
      const value = number(row.value), weight = number(row.weight);
      if (value === null || value < minimum || value > maximum || weight === null || weight < 0) {
        return { error: 'Bitte gültige Noten und Gewichte ab 0 eingeben.' };
      }
      if (weight === 0) continue;
      sum += value * weight;
      weights += weight;
      count++;
    }
    if (!Number.isFinite(sum) || !Number.isFinite(weights)) return { error: 'Die eingegebenen Werte sind zu groß.' };
    return { value: weights > 0 ? sum / weights : null, weights, count };
  }
  function errorQuotient(errors, words) {
    const e = number(errors), w = number(words);
    if (e === null || e < 0 || w === null || w <= 0 || !Number.isInteger(w)) return null;
    const result = e / w * 100;
    return Number.isFinite(result) ? result : null;
  }
  function linearGrade(points, maximum) {
    const p = number(points), m = number(maximum);
    if (p === null || m === null || m <= 0 || p < 0 || p > m) return null;
    return 6 - 5 * p / m;
  }
  const api = { number, weightedAverage, errorQuotient, linearGrade };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.NotenrechnerMath = api;
})(typeof window !== 'undefined' ? window : globalThis);
