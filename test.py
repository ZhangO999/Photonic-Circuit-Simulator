from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence

'''
Name:   Oliver Zhang
SID:    520651281
Unikey: ozha8307

This test program checks if the set_pulse_sequence function is implemented
correctly.

You can modify this scaffold as needed (changing function names, parameters,
or implementations...), however, DO NOT ALTER the code in circuit_for_testing
file, which provides the circuit. The circuit can be retrieved by calling
get_my_lasercircuit(), and it should be used as an argument for the
set_pulse_sequence function when testing.

Make sure to create at least six functions for testing: two for positive cases,
two for negative cases, and two for edge cases. Each function should take
different input files.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''


def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Positive test case to verify the set_pulse_sequence function.
    Configures the freq. and dir. of all 3 emitters on the circuit with 
    "realistic/reasonable" frequency values and varied directions.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    # Check if emitters' pulse sequence are correctly set up
    emitters = my_circuit.get_emitters()
    assert emitters[0].frequency == 100, f'Test case 1 failed. Expected: ' \
    'Emitter A frequency --> 100; got: {emitters[0].get_frequency()}'

    assert emitters[0].direction == 'E', f'Test case 1 failed. Expected: ' \
    'Emitter A direction --> E; got: {emitters[0].get_direction()}'

    assert emitters[1].frequency == 256, f'Test case 1 failed. Expected: ' \
    'Emitter B frequency --> 256; got: {emitters[1].get_frequency()}'

    assert emitters[1].direction == 'S', f'Test case 1 failed. Expected: ' \
    'Emitter B direction --> S; got: {emitters[1].get_direction()}'
    
    assert emitters[2].frequency == 200, f'Test case 1 failed. Expected: ' \
    'Emitter C frequency --> 300; got: {emitters[2].get_frequency()}'

    assert emitters[2].direction == 'W', f'Test case 1 failed. Expected: ' \
    'Emitter C direction --> W; got: {emitters[2].get_direction()}'
    
    print(f"Test case 1 passed with input file {pulse_file_path}")

    # close the file
    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Positive test case to verify the set_pulse_sequence function.
    Configures the freq. and dir. of all 3 emitters on the circuit
    with huge and tiny values and all North direction.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    emitters = my_circuit.get_emitters()
    assert emitters[0].frequency == 2, f'Test case 2 failed. Expected: ' \
    'Emitter A frequency --> 25; got: {emitters[0].get_frequency()}'

    assert emitters[0].direction == 'N', f'Test case 2 failed. Expected: ' \
    'Emitter A direction --> N; got: {emitters[0].get_direction()}'

    assert emitters[1].frequency == 1, f'Test case 2 failed. Expected: ' \
    'Emitter B frequency --> 600; got: {emitters[1].get_frequency()}'

    assert emitters[1].direction == 'N', f'Test case 2 failed. Expected: ' \
    'Emitter B direction --> N; got: {emitters[1].get_direction()}'

    assert emitters[
        2].frequency == 99999999999999999999999999999999999999, f'Test case' \
         '2 failed. Expected: Emitter C frequency --> 600; got: ' \
         '{emitters[2].get_frequency()}'

    assert emitters[2].direction == 'N', f'Test case 2 failed. Expected: ' \
    'Emitter C direction --> N; got: {emitters[2].get_direction()}'

    print(f"Test case 2 passed with input file {pulse_file_path}")

    file_obj.close()


def negative_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Negative test case to verify the set_pulse_sequence function.
    Testing if we get the correct error message if the frequency of emitter A
    is negative (invalid frequency).

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    try:
        set_pulse_sequence(my_circuit, file_obj)
        print('Test case 3 passed!')
        return None
    except ValueError as e:  # Invalid frequency -100 for emitter A
        assert str(e) == "Error: frequency must be greater than zero", 'Test'\
            ' case 3 failed: incorrect error msg output'

    file_obj.close()


def negative_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Negative test case to verify the set_pulse_sequence function.
    Testing if we get the correct error message if the symbol of emitter A 
    is not 'A'-'J' (invalid symbol).

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    try:
        set_pulse_sequence(my_circuit, file_obj)
        print('Test case 4 passed!')
        return None
    except ValueError as e:  # Invalid symbol Z for emitter A
        assert str(
            e) == "Error: Symbol is not between A-J", "Test case 4 failed: " \
            " incorrect error msg output"

    file_obj.close()


def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Edge test case to verify the set_pulse_sequence function.
    Testing if all emitters in the circuit would still have their pulse 
    sequences set if there were a newline gap between each sequence.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    emitters = my_circuit.get_emitters()
    assert emitters[0].is_pulse_sequence_set(), 'Test case 5 failed.'
    assert emitters[0].frequency == 10, 'Test case 5 failed.'
    assert emitters[0].direction == 'S', 'Test case 5 failed.'

    assert emitters[1].is_pulse_sequence_set(), 'Test case 5 failed.'
    assert emitters[1].frequency == 256, 'Test case 5 failed.'
    assert emitters[1].direction == 'S', 'Test case 5 failed.'

    assert emitters[2].is_pulse_sequence_set(), 'Test case 5 failed.'
    assert emitters[2].frequency == 256, 'Test case 5 failed.'
    assert emitters[2].direction == 'W', 'Test case 5 failed.'
    print(f"Test case 5 passed with input file {pulse_file_path}")

    file_obj.close()


def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Edge test case to verify the set_pulse_sequence function handles 
    more pulse sequences than emitters. Testing input file with more pulse
    sequences that there are emitters on board with pulse sequence for
    non-existent emitter E combing before C → our 3 emitters should still 
    be set.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''

    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    # All emitters A,B,C should have been set, with no additional ones
    assert len(my_circuit.emitters) == 3, 'Test case 6 failed.'

    # Check only the valid sequences were set correctly
    emitters = my_circuit.get_emitters()
    assert emitters[0].is_pulse_sequence_set(), 'Test case 6 failed.'
    assert emitters[0].frequency == 100, 'Test case 6 failed.'
    assert emitters[0].direction == 'E', 'Test case 6 failed.'

    assert emitters[1].is_pulse_sequence_set(), 'Test case 6 failed.'
    assert emitters[1].frequency == 256, 'Test case 6 failed.'
    assert emitters[1].direction == 'S', 'Test case 6 failed.'

    assert emitters[2].is_pulse_sequence_set(), 'Test case 6 failed.'
    assert emitters[2].frequency == 256, 'Test case 6 failed.'
    assert emitters[2].direction == 'W', 'Test case 6 failed.'

    print(f"Test case 6 passed with input file {pulse_file_path}")

    file_obj.close()


if __name__ == '__main__':
    # Run each function for testing
    positive_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence.in')
    positive_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_2.in')
    negative_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence_3.in')
    negative_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_4.in')
    edge_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence_5.in')
    edge_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_6.in')

