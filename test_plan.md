Name:   Oliver Zhang
SID:    520651281
Unikey: ozha8307

**Test Cases**
Table 1. Summary of test cases for parse_pulse_sequence
| File Name             | Function Name   | Description                                                                                                                                                                                       | Expected Error Message(s) (if any) | Pass/Fail |
| --------------------- | ----------------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | --------- |
| pulse_sequence.in     | positive_test_1 | Positive Case - Configure the freq. and dir. of all 3 emitters on the circuit with "realistic/reasonable" frequency values and varied directions                                                  | N/A                                | Pass      |
| pulse_sequence_2.in   | positive_test_2 | Positive Case - Configure the freq. and dir. of all 3 emitters on the circuit with huge and tiny values and all North direction                                                                   | N/A                                | Pass      |
| pulse_sequence_3.in   | negative_test_1 | Negative Case - Testing if we get the correct error message if the frequency of emitter A is negative (invalid frequency)                                                                         | N/A                                | Pass      |
| pulse_sequence_4.in   | negative_test_2 | Negative Case - Testing if we get the correct error message if the symbol of emitter A is not 'A'-'J' (invalid symbol)                                                                            | N/A                                | Pass      |
| pulse_sequence_5.in   | edge_test_1     | Edge Case - Testing if all emitters in the circuit would still have their pulse sequences set if there were a newline gap between each sequence                                                   | AssertionError: Test case 5 failed.| Fail      |
| pulse_sequence_6.in   | edge_test_2     | Edge Case - Testing input file with more pulse sequences that there are emitters on board with pulse sequence for non-existent emitter E combing before C → our 3 emitters should still be set.   | N/A                                | Pass      |  
