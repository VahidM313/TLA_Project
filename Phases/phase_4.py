import json

def Star(fa):
    # Load the input FA from JSON
    with open(fa, 'r') as fa_file:
        fa_data = json.load(fa_file)
    
    # Extract the states, input symbols, and transitions from the input FA
    states = eval(fa_data['states'])
    input_symbols = eval(fa_data['input_symbols'])
    transitions = fa_data['transitions']
    initial_state = fa_data['initial_state']
    final_states = eval(fa_data['final_states'])

    # Create a new state for the language star, add it to the set of states
    new_initial_state = 'q*'
    states.add(new_initial_state)

    # Create a new final state for the language star, add it to the set of states
    new_final_state = 'qf'
    states.add(new_final_state)

    # Add transitions form q* to the old initial state and qf by lambda.
    transitions[new_initial_state] = { "": f"{{'{initial_state}','{new_final_state}'}}" }

    # Add transition form qf to q* by lambda.
    transitions[new_final_state] = { "":  f"{{'{new_initial_state}'}}" }


    # Add transitions from the final states of the input FA to the new final state (qf)
    for fs in final_states:
            transitions[fs].update({ "":  f"{{'{new_final_state}'}}" })

    # Convert to strings for JSON output
    states_str = str(set(sorted(list(states)))).replace(" ","")
    input_symbols_str = str(set(sorted(list(input_symbols)))).replace(" ","")
    initial_state_str = new_initial_state.replace(" ","")
    final_state_str = "{'"+(new_final_state).replace(" ","")+"'}"

    # Create a new dictionary for the output FA and save to JSON
    fa_star_data = {
        'states': states_str,
        'input_symbols': input_symbols_str,
        'transitions': transitions,
        'initial_state': initial_state_str,
        'final_states': final_state_str,
    }

    with open('Phases/phase_4.json', 'w') as fa_star_file:
        json.dump(fa_star_data, fa_star_file, indent=2)

    return json.dumps(fa_star_data)


def Concat(fa1,fa2):
    # Load the input FAs from JSON
    with open(fa1, 'r') as fa_file:
        fa1_data = json.load(fa_file)
    with open(fa2, 'r') as fa_file:
        fa2_data = json.load(fa_file)

    #replace all q in FA2 with r
    def replace_q_with_r(obj):
        if isinstance(obj, dict):
            return {k.replace('q', 'r'): replace_q_with_r(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [replace_q_with_r(elem) for elem in obj]
        elif isinstance(obj, str):
            return obj.replace('q', 'r')
        else:
            return obj

    # Apply the function to the data
    new_fa2_data = replace_q_with_r(fa2_data)
    # Write the updated data to a new JSON file
    with open('output.json', 'w') as f:
        json.dump(new_fa2_data, f, indent=2)
    
#main

#Star("samples/phase4-sample/star/in/FA.json")
Concat("samples/phase4-sample/concat/in/FA1.json","samples/phase4-sample/concat/in/FA2.json")
