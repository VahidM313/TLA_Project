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

    #...
    #for transitions
    #...

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


#main

Star("samples/phase4-sample/star/in/FA.json")
