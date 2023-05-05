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


#main

Star("samples/phase4-sample/star/in/FA.json")
