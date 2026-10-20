const {test} = require('node:test');
const assert = require('node:assert/strict');
const math = require('../assets/calculations.js');
test('Gewichtete Schulnoten und Notenpunkte entsprechen den veröffentlichten Beispielen', () => {
  assert.equal(math.weightedAverage([{value:'2',weight:'2'}, {value:'3',weight:'1'}], 1, 6).value, 7/3);
  assert.equal(math.weightedAverage([{value:'12',weight:'1'}, {value:'10',weight:'1'}, {value:'14',weight:'2'}], 0, 15).value, 12.5);
  assert.equal(math.weightedAverage([{value:'2',weight:'40'}, {value:'3',weight:'60'}], 1, 6).value, 2.6);
});
test('Kommawerte, leere Zeilen und explizit ausgeschlossene Noten', () => {
  assert.equal(math.weightedAverage([{value:'2,5',weight:'0,5'}, {value:'1,5',weight:'0,5'}, {value:'',weight:'1'}], 1, 6).value, 2);
  assert.equal(math.weightedAverage([{value:'6',weight:'0'}, {value:'2',weight:'1'}], 1, 6).value, 2);
  assert.equal(math.weightedAverage([{value:'0',weight:'1'}], 0, 15).value, 0);
  assert.equal(math.weightedAverage([{value:'2',weight:'0'}], 1, 6).value, null);
});
test('Ungültige Eingaben werden nicht stillschweigend als richtige Noten akzeptiert', () => {
  for (const value of ['2abc','Infinity','NaN','2e3','7','0','-2']) assert.ok(math.weightedAverage([{value,weight:'1'}], 1, 6).error);
  for (const weight of ['-1','NaN','']) assert.ok(math.weightedAverage([{value:'2',weight}], 1, 6).error);
});
test('Fehlerquotient: Nullfehler, halbe Fehler und ungültige Wortzahlen', () => {
  assert.equal(math.errorQuotient('6', '200'), 3);
  assert.equal(math.errorQuotient('0', '100'), 0);
  assert.equal(math.errorQuotient('0,5', '100'), 0.5);
  for (const words of ['0','-1','','100,5','Infinity']) assert.equal(math.errorQuotient('6', words), null);
  assert.equal(math.errorQuotient('-1','100'), null);
});
test('Linearer Schlüssel: Endpunkte, Rechenbeispiel und Eingabegrenzen', () => {
  assert.equal(math.linearGrade('0','100'), 6);
  assert.equal(math.linearGrade('100','100'), 1);
  assert.equal(math.linearGrade('66','100'), 2.7);
  for (const [p,m] of [['-1','100'],['101','100'],['1','0'],['','100']]) assert.equal(math.linearGrade(p,m),null);
});
