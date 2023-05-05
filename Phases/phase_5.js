const FA = require("../samples/phase5-sample/in/FA.json");
let result = FAtoRegex(FA);
console.log(result) 

function FAtoRegex(FA) {

  const states = FA.states.replace(/'|{|}/g, "").split(",");
  const input_symbols = FA.input_symbols.replace(/'|{|}/g, "").split(",");
  const initial_state = FA.initial_state;
  const final_states = FA.final_states.replace(/'|{|}/g, "").split(",");

  let transitions = {};
  for (let state in FA.transitions) {
    transitions[state] = {};
    for (let symbol in FA.transitions[state]) {
      let destinations = FA.transitions[state][symbol];
      destinations = destinations.replace(/'/g, '"');
      destinations = destinations.replace(/{/g , '[')
      destinations = destinations.replace(/}/g , ']')
      destinations = JSON.parse(destinations);
      transitions[state][symbol] = destinations;
    }
  }


  // Create an equation system
  let equations = {};
  for (let state of states) {
    let rhs = "";
    if (transitions.hasOwnProperty(state)) {
      for (let symbol in transitions[state]) {
        for (let dest of transitions[state][symbol]) {
          rhs += symbol + dest + "+";
        }
      }
    }
    if (final_states.includes(state)) {
      rhs += "ε+";
    }
    if (rhs.length > 0) {
      rhs = rhs.slice(0, -1);
    }
    equations[state] = rhs;
  }

  // Solve the equation system using Arden's Lemma
  function applyArden(equation) {
    let parts = equation.split("+");
    let r = "";
    let q = "";
    for (let part of parts) {
      if (part.includes("q")) {
        r += part.replace("q", "") + "+";
      } else {
        q += part;
      }
    }
    r = r.slice(0, -1);
    return q + (r === "" ? "" : r + "*");
  }

  // Solve the system of equations using Arden's Lemma
  for (let state in equations) {
    let equation = equations[state];
    while (equation.includes("q")) {
      let start = equation.indexOf("q");
      let end = start + 1;
      while (end < equation.length && equation[end] !== "+" && equation[end] !== ")") {
        end++;
      }
      let subState = equation.slice(start, end);
      let subEquation = equations[subState];
      equation = equation.replace(subState, "(" + subEquation + ")");
    }
    equations[state] = applyArden(equation);
  }

  return equations[initial_state];
}
