(() => {
  'use strict';
  let mode = 'np', rowId = 0;
  const rows = document.getElementById('rows');
  const grade = document.getElementById('avgGrade');
  const meta = document.getElementById('avgMeta');
  const count = document.getElementById('avgCount');
  const format = n => n.toLocaleString('de-DE', {minimumFractionDigits: 2, maximumFractionDigits: 2});

  function calculate() {
    const values = [...rows.children].map(row => ({value: row.querySelector('.val').value, weight: row.querySelector('.weight').value}));
    const result = NotenrechnerMath.weightedAverage(values, mode === 'np' ? 0 : 1, mode === 'np' ? 15 : 6);
    [...rows.children].forEach(row => {
      const value = NotenrechnerMath.number(row.querySelector('.val').value);
      const weight = NotenrechnerMath.number(row.querySelector('.weight').value);
      const filled = row.querySelector('.val').value.trim() !== '';
      row.querySelector('.val').setAttribute('aria-invalid', String(filled && (value === null || value < (mode === 'np' ? 0 : 1) || value > (mode === 'np' ? 15 : 6))));
      row.querySelector('.weight').setAttribute('aria-invalid', String(filled && (weight === null || weight < 0)));
    });
    grade.textContent = result.value == null ? '—' : format(result.value);
    grade.classList.toggle('avg-empty', result.value == null);
    meta.textContent = result.error || (result.value == null ? 'Noten eingeben; mindestens ein Gewicht muss größer als 0 sein.' : mode === 'np' ? 'Notenpunkte · rechnerischer Mittelwert' : 'Schulnote · rechnerischer Mittelwert');
    count.textContent = result.value == null ? '' : `Aus ${result.count} Leistungen · Summe der Gewichte: ${format(result.weights)}`;
    document.getElementById('avgResult').style.background = 'var(--primary-50)';
    document.getElementById('avgResult').style.color = 'var(--text)';
    document.getElementById('averageFormula').textContent = result.value == null ? '' : values.filter(r => String(r.value).trim() !== '' && NotenrechnerMath.number(r.weight) > 0).map(r => `${r.value} × ${r.weight}`).join(' + ') + `; geteilt durch ${format(result.weights)} = ${format(result.value)}`;
  }

  function makeRow(label = '', value = '', weight = '1') {
    const row = document.createElement('div');
    row.className = 'avg-row';
    const id = ++rowId;
    for (const [className, title, initial] of [['subj', 'Leistung', label], ['val', mode === 'np' ? 'Notenpunkte' : 'Schulnote', value], ['weight', 'Gewicht', weight]]) {
      const field = document.createElement('label');
      field.className = 'average-field';
      const caption = document.createElement('span');
      caption.textContent = title;
      const input = document.createElement('input');
      input.type = 'text'; input.className = className; input.id = `average-${id}-${className}`;
      input.value = initial; input.autocomplete = 'off';
      if (className !== 'subj') input.inputMode = 'decimal';
      if (className === 'subj') input.placeholder = 'Optional';
      input.addEventListener('input', calculate);
      field.append(caption, input); row.append(field);
    }
    const remove = document.createElement('button');
    remove.type = 'button'; remove.className = 'remove-btn'; remove.textContent = '×';
    remove.setAttribute('aria-label', 'Leistung entfernen');
    remove.addEventListener('click', () => {
      if (rows.children.length === 1) {
        row.querySelector('.val').value = ''; row.querySelector('.weight').value = '1';
      } else row.remove();
      calculate();
    });
    row.append(remove); rows.append(row);
  }
  function setMode(value) {
    mode = value;
    for (const [id, selected] of [['modeNP', mode === 'np'], ['modeNote', mode === 'note']]) {
      document.getElementById(id).classList.toggle('active', selected);
      document.getElementById(id).setAttribute('aria-selected', String(selected));
    }
    rows.replaceChildren(); makeRow(); makeRow(); calculate();
  }
  document.getElementById('modeNP').addEventListener('click', () => setMode('np'));
  document.getElementById('modeNote').addEventListener('click', () => setMode('note'));
  document.getElementById('addRow').addEventListener('click', () => {makeRow(); rows.lastElementChild.querySelector('.val').focus();});
  document.querySelectorAll('[data-average-example]').forEach(button => button.addEventListener('click', () => {
    const examples = {
      written: {mode: 'note', rows: [['Schriftlich', '2', '2'], ['Mündlich', '3', '1']]},
      exams: {mode: 'np', rows: [['Klausur 1', '12', '1'], ['Klausur 2', '10', '1'], ['Klausur 3', '14', '2']]},
      semesters: {mode: 'note', rows: [['1. Halbjahr', '2', '40'], ['2. Halbjahr', '3', '60']]}
    };
    const example = examples[button.dataset.averageExample];
    setMode(example.mode); rows.replaceChildren(); example.rows.forEach(row => makeRow(...row)); calculate();
  }));
  setMode('np');
})();
