const data = require("./../samples/phase2-sample/in/input1.json");

// parsing json

const states = data.states.replace(/'|{|}/g, "").split(",");
const input_symbols = data.input_symbols.replace(/'|{|}/g, "").split(",");
const initial_state = data.initial_state;
const final_states = data.final_states.replace(/'|{|}/g, "").split(",");
let transitions = Object.entries(data.transitions);

// convert transition object of json to transition table

let transTable = [];
let column = [null, "", ""];

transitions = transitions.map((i) => {
  i[1] = Object.entries(i[1]);
  i[1] = i[1].map((j) => {
    j[1] = j[1].replace(/'|{|}/g, "").split(",");
    return j;
  });
  column[0] = i[0];
  i[1].forEach((element) => {
    if (element[0] === input_symbols[0]) column[1] += element[1];
    else if (element[0] === input_symbols[1]) column[2] += element[1];
  });
  transTable.push(column);
  column = [null, "", ""];
  i = i[1];
  return i;
});

console.table(transTable);

// remove unreachable states

let reachableState = [];

for(let i of transTable) {
  if(i[0] === "q0") {
    reachableState.push("q0");
    continue;
  }
  for(let j of transTable) {
    if(i[0] !== j[0]) {
      if(i[0] === j[1] || i[0] === j[2]) {
        reachableState.push(i[0]);
        break;
      }
    }
  }
}

transTable = transTable.filter(s => reachableState.includes(s[0]));

console.table(transTable);