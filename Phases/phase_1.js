const data = require("./../samples/phase1-sample/in/input1.json");

// parsing json 

const states = data.states.replace(/'|{|}/g, "").split(",");
const input_symbols = data.input_symbols.replace(/'|{|}/g, "").split(",");
const initial_state = data.initial_state;
const final_states = data.final_states.replace(/'|{|}/g, "").split(",");
let transitions = Object.entries(data.transitions);

// convert transition object of json to transition table

let transTable = [];
let column = [null, "", "", ""];

transitions = transitions.map((i) => {
  i[1] = Object.entries(i[1]);
  i[1] = i[1].map((j) => {
    j[1] = j[1].replace(/'|{|}/g, "").split(",");
    return j;
  });
  column[0] = i[0];
  i[1].forEach((element) => {
    if (element[0] === "") element[0] = "λ";
    if (element[0] === "λ") column[3] += element[1];
    else if (element[0] === "a") column[1] += element[1];
    else if (element[0] === "b") column[2] += element[1];
  });
  transTable.push(column);
  column = [null, "", "", ""];
  i = i[1];
  return i;
});

console.log(final_states);
console.table(transTable);
