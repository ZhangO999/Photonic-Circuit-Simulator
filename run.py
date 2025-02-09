import sys
import input_parser
import sorter
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit

'''
Name:   Oliver Zhang
SID:    520651281
Unikey: ozha8307

run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Returns whether or not '-RUN-MY-CIRCUIT' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    # loop over args list, check if any element matches string "-RUN-MY-CIRCUIT"
    i = 0 
    while i < len(args):
        if args[i] == "-RUN-MY-CIRCUIT":
            return True
        i += 1
    # only execute if no matches found in args:   
    return False


def is_add_my_mirrors_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Returns whether or not '-ADD-MY-MIRRORS' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    # loop over args list, check if any element matches string "-ADD-MY-MIRRORS"
    i = 0 
    while i < len(args):
        if args[i] == "-ADD-MY-MIRRORS":
            return True
        i += 1
    # only execute if no matches found in args:   
    return False
    


def initialise_circuit() -> LaserCircuit:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Gets the inputs for the board size, emitters and receivers and processes
    it to create a LaserCircuit instance and return it. You should be using
    the functions you have implemented in the input_parser module to handle
    validating each input.

    Returns
    -------
    A LaserCircuit instance with a width and height specified by the user's
    inputted size. The circuit should also include each emitter and receiver
    the user has inputted.
    '''
    print("Creating circuit board...")
    board_created = False
    while not(board_created):
        board_size = input("> ")
        dim = input_parser.parse_size(board_size) # check valid board dimensions
        if dim is None: 
            continue # skip iteration to re-prompt if invalid input; only proceed with valid dimensions.
        width, height = dim
        circuit = LaserCircuit(width, height)
        print(f"{width}x{height} board created.\n")
        board_created = True
    
    print("Adding emitter(s)...")
    emitters_added = 0 
    while emitters_added < 10:
        emitter_input = input("> ")
        if emitter_input == "END EMITTERS":
            break

        emitter = input_parser.parse_emitter(emitter_input) # checks inputs are valid and returns emitter instance.
        if emitter is not None:
            emitter_successfully_added = circuit.add_emitter(emitter)
            if emitter_successfully_added:
                emitters_added += 1
        else:
            continue

    print(f"{emitters_added} emitter(s) added.\n")

    print("Adding receiver(s)...")
    receivers_added = 0 
    while receivers_added < 10:
        receiver_input = input("> ")
        if receiver_input == "END RECEIVERS":
            break

        receiver = input_parser.parse_receiver(receiver_input) # checks inputs are valid and returns receiver instance.
        if receiver is not None:
            receiver_successfully_added = circuit.add_receiver(receiver)
            if receiver_successfully_added:
                receivers_added += 1
        else:
            continue

    print(f"{receivers_added} receiver(s) added.\n")

    return circuit



def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Handles setting the pulse sequence of the circuit. 
    The lines for the pulse sequence will come from the a file named
    /home/input/<file_name>.in. 
    You should be using the functions you have implemented in the input_parser module 
    to handle validating lines from the file.

    Parameter
    ---------
    circuit - The circuit to set the pulse sequence for.
    file_obj - A file like object returned by the open()
    '''
    print("Setting pulse sequence...")
    line_num = 0
    while True: # keep reading lines for however many lines there are in the file_obj (unknown beforehand)
        line_num += 1 # track the line num
        # process our iteration's line:
        line = file_obj.readline().rstrip("\n")
        if not line: # empty line (truthiness) -> stop reading if we've reached last line
            break 
        
        # cook up list of emitters whose pulse_sequences have yet to been set:
        unset_emitters = []
        i = 0
        while i < len(circuit.emitters):
            emitter = circuit.emitters[i]
            if not emitter.is_pulse_sequence_set():
                unset_emitters.append(emitter)
            i += 1
        # now sort alphabetically by symbol: 
        unset_emitters = sorter.sort_emitters_by_symbol(unset_emitters)
        
        
        # now pretty print the list of unset_emitters symbols in current iteration, seperated by commas:
        j = 0 
        u_emitters_str = ""
        while j < len(unset_emitters):
            u_emitter_symbol = unset_emitters[j].symbol
            u_emitters_str += u_emitter_symbol + ", "
            j += 1
        u_emitters_str = u_emitters_str.strip(", ") # should now have cooked up f-str like "A, B, ..., J"
        print(f"-- ({u_emitters_str})")
        
        print(f"Line {line_num}: {line}")
        # parse pulse sequence to validate inputs: 
        pulse_sequence = input_parser.parse_pulse_sequence(line.strip()) # should return whatever error msg if it exists

        # all parse_pulse_sequence() checks passed?
        # No, at least one of them failed:
        if pulse_sequence is None: # line contains invalid sequence -> triggers one of the input_parser error msgs -> skip
            continue 
        # Yes -> 2 further checks: 
        symbol, frequency, direction = pulse_sequence # extract tokens if all valid

        # does the corresponding emitter w/symbol exist in the circuit? If so, has that emitter already been set? If not, set it.
        k = 0 
        matching_emitter_found = False
        sequence_already_set = False
        while k < len(circuit.emitters):
            emitter = circuit.emitters[k]
            if (emitter.symbol == symbol): # check 1 Y -> emitter w/symbol exists
                matching_emitter_found = True   
                # check 2:
                if not(emitter.is_pulse_sequence_set()): # check 2 N -> emitter not set -> SET IT
                    emitter.set_pulse_sequence(frequency, direction)
                else: # check 2 Y -> already set 
                    print(f"Error: emitter '{symbol}' already has its pulse sequence set")
                    sequence_already_set = True
                    break # to (*)
            k += 1
        # (*)
        if sequence_already_set: 
            continue 
            
        # Check 2 N -> emitter w/symbol not found -> next iteration
        if not matching_emitter_found:
            print(f"Error: emitter '{symbol}' does not exist")
            continue
    
    print("Pulse sequence set.")
        
        

    


def add_mirrors(circuit: LaserCircuit) -> None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Handles adding the mirrors into the circuit. You should be using the
    functions you have implemented in the input_parser module to handle
    validating each input. 
    
    Parameters
    ----------
    circuit - the laser circuit to add the mirrors into
    '''
    print("Adding mirror(s)...")
    mirrors_added = 0 
    while True: 
        mirror_input = input("> ")
        if mirror_input == "END MIRRORS":
            break
        
        mirror = input_parser.parse_mirror(mirror_input) # parse input params, and create mirror if valid
        if mirror is None: 
            continue # if input is invalid, skip to the next iteration
        
        # check if the mirror can be added to the circuit
        if circuit.add_mirror(mirror):
            mirrors_added += 1 # increment the count only if mirror was added succesfullly
        
    print(f"{mirrors_added} mirror(s) added.") 
    


def main(args: list[str]) -> None:
    # only requires implementation once you reach GET-MY-INPUTS
    # will require extensions in RUN-MY-CIRCUIT and ADD-MY-MIRRORS
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''

    circuit = initialise_circuit()

    if is_add_my_mirrors_enabled(args):
        print("<ADD-MY-MIRRORS FLAG DETECTED!>\n")
        add_mirrors(circuit)
        print()
    circuit.print_board() # print a circuit afterwards irrespective of mirrors added
    print()
    if is_run_my_circuit_enabled(args):
        print("<RUN-MY-CIRCUIT FLAG DETECTED!>\n")
        PS_PATH = "/home/input/pulse_sequence.in" # pulse sequence input file path (for reading)

        try:
            with open(PS_PATH, 'r') as file: 
                set_pulse_sequence(circuit, file) 
                LaserCircuit.run_circuit(circuit)
        except FileNotFoundError: 
            print(f"Error: -RUN-MY-CIRCUIT flag detected but {PS_PATH} does not exist")
            return None
    


if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''
    main(sys.argv)
    

