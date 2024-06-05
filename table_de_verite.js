function generateTruthTable(n) {
  const results = [];
  for (let i = 0; i < Math.pow(2, n); i++) {
    const row = [];
    for (let j = n - 1; j >= 0; j--) {
      row.push(i & (1 << j) ? true : false);
    }
    results.push(row);
  }
  return results;
}

function implies(p, q) {
  return !p || q;
}
function not(p) {
  return !p;
}
function and(p, q) {
  return p && q;
}
function or(p, q) {
  return p || q;
}
function equi(p, q) {
  return p == q ? true : false;
}

function checkPropositions() {
  const truthTable = generateTruthTable(3); // 3 propositions de base: p, q, r
  const results = [];

  for (let i = 0; i < truthTable.length; i++) {
    const p = truthTable[i][0];
    const q = truthTable[i][1];
    const r = truthTable[i][2];

    const proposition1 = implies(p, implies(q, r));
    const proposition2 = implies(not(q), not(p));
    const proposition3 = p;
    const conclusion = r;

    const allPropositionsTrue = proposition1 && proposition2 && proposition3;

    results.push({
      p: p,
      q: q,
      r: r,
      proposition1: proposition1,
      proposition2: proposition2,
      proposition3: proposition3,
      conclusion: conclusion,
      allPropositionsTrue: allPropositionsTrue,
    });
    const allPropositionsVerif =
      proposition1 && proposition2 && proposition3 && conclusion;
    if (allPropositionsVerif) {
      console.log("Propositions logiques vraies");
    } else {
      console.log("Propositions logiques fausses");
    }
  }

  return results;
}

function displayResults(results) {
  results.forEach((row) => {
    console.log(
      ` ${row.p ? "T" : "F"}  |  ${row.q ? "T" : "F"}  |  ${
        row.r ? "T" : "F"
      }  |   ${row.proposition2 ? "T" : "F"}    |   ${
        row.proposition3 ? "T" : "F"
      }    |     ${row.conclusion ? "T" : "F"}     |         ${
        row.allPropositionsTrue ? "T" : "F"
      }`
    );
  });
  // console.log(results);
}

const results = checkPropositions();
displayResults(results);
