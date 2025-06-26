# Photonic Circuit Simulator

## Overview
This is a **Python-based photonic circuit simulation**, designed to model the movement of photons through an interactive circuit of emitters, receivers, and mirrors. Users can use the provided input files to modify simulation parameters. 

## Features
* **Circuit Board Setup** – Users can define a circuit grid and place emitters, receivers, and mirrors.  
*  **Customizable Photon Inputs** – Accepts user-defined emitter frequencies and pulse sequences.  
* **Photon Propagation Simulation** – Simulates light movement, interactions with components, and energy absorption.  
* **Command-Line Interface** – Interactive setup through user inputs.  
* **Dynamic Visualization** – Displays the board state at each step of the simulation.  
* **Automated Testing** – Includes test scripts for validating the circuit's behavior.  



## Installation & Usage
- Ensure you have **Python 3.11.8** (or later) installed.
- Follow the command-line prompts to set-up the circuit and run a simulation.


#### Example Usage
```python
$ python3 run.py
Creating circuit board...
> #18 6
18x6 board created.

Adding emitter(s)...
> #A 2 2
> #B 8 1
> #END EMITTERS
2 emitter(s) added.

Adding receiver(s)...
> #R0 15 2
> #R1 8 4
> #END RECEIVERS
2 receiver(s) added.

+------------------+
|                  |
|        B         |
|  A            0  |
|                  |
|        1         |
|                  |
+------------------+

<RUN-MY-CIRCUIT FLAG DETECTED!>

Running the circuit...
