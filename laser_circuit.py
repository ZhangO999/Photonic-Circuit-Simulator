import sorter
from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from board_displayer import BoardDisplayer

'''
Name:   Oliver Zhang
SID:    520651281
Unikey: ozha8307

LaserCircuit - Responsible for storing all the components of the circuit and
handling the computation of running the circuit. It's responsible for delegating
tasks to the specific components e.g. making each emitter emit a photon, getting
each photon to move and interact with components, etc. In general, this class is
responsible for handling any task related to the circuit.

You are free to add more attributes and methods, as long as you aren't
modifying the existing scaffold.
'''


class LaserCircuit:
    def __init__(self, width: int, height: int):
        '''
        Initialise a LaserCircuit instance given a width and height. All
        lists of components and photons are empty by default.
        board_displayer is initialised to a BoardDisplayer instance. clock is
        0 by default.

        emitters:        list[Emitter]  - all emitters in this circuit
        receivers:       list[Receiver] - all receivers in this circuit
        photons:         list[Photon]   - all photons in this circuit
        mirrors:         list[Mirror]   - all mirrors in this circuit
        width:           int            - the width of this circuit board
        height:          int            - the height of this circuit board
        board_displayer: BoardDisplayer - helper class for storing and
                                          displaying the circuit board
        clock:           int            - a clock keeping track of how many
                                          nanoseconds this circuit has run for

        Parameters
        ----------
        width  - the width to set this circuit board to
        height - the width to set this circuit board to
        '''
        self.emitters = []
        self.receivers = []
        self.photons = []
        self.mirrors = []
        self.width = width
        self.height = height
        # initialise an instance of an embedded-object.
        self.board_displayer = BoardDisplayer(self.width, self.height)
        self.clock = 0

    def emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Gets each emitter in this circuit's list of emitters to emit a photon.
        The photons emitted should be added to this circuit's photons list.
        '''
        if len(self.emitters) == 0:  # don't bother emitting anything if list is empty.
            return None
        i = 0
        while i < len(self.emitters):
            photon_emitted = self.emitters[i].emit_photon()
            self.photons.append(photon_emitted)
            i += 1

    def is_finished(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns whether or not this circuit has finished running. The
        circuit is finished running if every photon in the circuit has been
        absorbed.

        Returns
        -------
        True if the circuit has finished running or not, else False.
        '''
        # check if there are no photons in the circuit or if all photons are
        # absorbed
        if len(self.photons) == 0:
            return True

        # check if each photon has been absorbed; running not done iff
        # ∃photon(photon not absorbed)
        i = 0
        while i < len(self.photons):
            photon = self.photons[i]
            if not photon.is_absorbed():
                return False  # counter-example -> NOT DONE!
            i += 1
        return True

    def print_emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for each emitter emitting a photon.

        It will also need to write the output into a
        /home/output/emit_photons.out output file.

        You can assume the /home/output/ path exists.
        '''
        print("0ns: Emitting photons.")
        i = 0
        output = ""
        sorted_emitters = sorter.sort_emitters_by_symbol(self.emitters)
        with open("/home/output/emit_photons.out", "w") as file:
            # each emitter in the circuit should be emitting a photon.
            while i < len(sorted_emitters):
                emitter = sorted_emitters[i]  # emitter that emitted photon[i]

                # cook up strings for full direction words:
                if emitter.direction == "N":
                    emitter_dir_word = "North"
                elif emitter.direction == "E":
                    emitter_dir_word = "East"
                elif emitter.direction == "S":
                    emitter_dir_word = "South"
                else:  # direction = "W"
                    emitter_dir_word = "West"

                output += f"{emitter.symbol}: {emitter.frequency}THz, {emitter_dir_word}\n"
                i += 1
            # cook up output string --> allows us to print + write to file only
            # once
            print(output)
            file.write(output)

    def print_activation_times(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the activation times for each receiver, sorted
        by activation time in ascending order. Any receivers that have not
        been activated should not be included.

        It will also need to write the output into a
        /home/output/activation_times.out output file.

        You can assume the /home/output/ path exists.
        '''
        print("Activation times:")
        # filter for activated receivers only:
        activated_receivers = []
        i = 0
        while i < len(self.receivers):
            receiver = self.receivers[i]
            if receiver.is_activated():
                activated_receivers.append(receiver)
            i += 1

        # now sort filtered list of receivers:
        sorted_receivers = sorter.sort_receivers_by_activation_time(
            activated_receivers)

        # now we may pretty print the sorted list and write to file.
        output = ""
        with open("/home/output/activation_times.out", "w") as file:
            j = 0
            while j < len(sorted_receivers):
                receiver = sorted_receivers[j]
                output += f"{receiver.symbol}: {receiver.activation_time}ns\n"
                j += 1
            # cook up output string --> allows us to print + write to file only
            # once.
            print(output)
            file.write(output)

    def print_total_energy(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the total energy absorbed for each receiver,
        sorted by total energy absorbed in descending order. Any receivers
        that have not been activated should not be included.

        It will also need to write the output into a
        /home/output/total_energy_absorbed.out output file.

        You can assume the /home/output/ path exists.
        '''
        print("Total energy absorbed:")
        # filter for activated receivers only:
        activated_receivers = []
        i = 0
        while i < len(self.receivers):
            receiver = self.receivers[i]
            if receiver.is_activated():
                activated_receivers.append(receiver)
            i += 1

        # now sort filtered list of receivers:
        sorted_receivers = sorter.sort_receivers_by_total_energy(
            activated_receivers)

        # now we may pretty print the sorted list and write to file.
        output = ""
        with open("/home/output/total_energy.out", "w") as file:
            j = 0
            while j < len(sorted_receivers):
                receiver = sorted_receivers[j]
                output += f"{receiver.symbol}: {receiver.total_energy:.2f}eV ({receiver.photons_absorbed})\n"
                j += 1
            # cook up output string --> allows us to print + write to file only
            # once.
            print(output)
            file.write(output)

    def print_board(self) -> None:
        '''Calls the print_board method in board_displayer.'''
        self.board_displayer.print_board()  # calls print_board on the EMBEDDED OBJECT.

    def get_collided_emitter(
            self,
            entity: Emitter | Receiver | Photon | Mirror | None) -> Emitter | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another emitter in the
        circuit.

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no emitter occupying entity's
        position.

        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        An emitter if it has the same position as entity, else None.
        '''
        i = 0
        # loop over all the emitters on the circuit.
        while i < len(self.emitters):
            # check same coords
            if self.emitters[i].x == entity.x and self.emitters[i].y == entity.y:
                return self.emitters[i]
            i += 1
        return None

    def get_collided_receiver(
            self,
            entity: Emitter | Receiver | Photon | Mirror | None) -> Receiver | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another receiver in the
        circuit.

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no receiver occupying entity's
        position.

        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A receiver if it has the same position as entity, else None.
        '''
        i = 0
        # loop over all the receivers on the circuit.
        while i < len(self.receivers):
            # check same coords
            if self.receivers[i].x == entity.x and self.receivers[i].y == entity.y:
                return self.receivers[i]
            i += 1
        return None

    def get_collided_mirror(self, entity: Emitter |
                            Receiver | Photon | Mirror | None) -> Mirror | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another mirror in the
        circuit.

        If it does, return the mirror already in the entity's position.
        Else, return None, indicating there is no mirror occupying entity's
        position.

        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A mirror if it has the same position as entity, else None.
        '''
        i = 0
        # loop over all the mirrors on the circuit.
        while i < len(self.mirrors):
            if self.mirrors[i].x == entity.x and self.mirrors[i].y == entity.y:  # check same coords
                return self.mirrors[i]
            i += 1
        return None

    def get_collided_component(
            self,
            photon: Photon) -> Emitter | Receiver | Mirror | None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Given a photon, returns the component it has collided with (if any).
        A collision occurs if the positions of photon and the component are
        the same.

        Parameters
        ----------
        photon - a photon to check for collision with the circuit's components

        Returns
        -------
        If the photon collided with a component, return that component.
        Else, return None.

        Hint
        ----
        Use the three collision methods above to handle this.
        '''
        # check collisions of our photon with the emitters on board:
        collided_emitter = self.get_collided_emitter(photon)
        if collided_emitter is not None:
            return collided_emitter

        # check collisions of our photon with the receivers on board:
        collided_receiver = self.get_collided_receiver(photon)
        if collided_receiver is not None:
            return collided_receiver

        # check collisions of our photon with the mirrors on board:
        collided_mirror = self.get_collided_mirror(photon)
        if collided_mirror is not None:
            return collided_mirror

        return None  # only run if previous checks don't return out early.

    def tick(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs a single nanosecond (tick) of this circuit. If the circuit has
        already finished, this method should return out early.

        Otherwise, for each photon that has not been absorbed, this method is
        responsible for moving it, updating the board to show its new position
        and checking if it collided with a component (and handling it if did
        occur). At the end, we then increment clock.
        '''
        self.clock += 1
        if self.is_finished():  # all photons on board have been absorbed
            return None
        # else: ≥1 photon not absorbed yet
        i = 0
        while i < len(self.photons):
            photon = self.photons[i]
            if not photon.is_absorbed(
            ):  # sanity check --> self.photons should already be non-absorbed ones
                # out of bounds already handled by .move() method
                photon.move(self.width, self.height)
                # check collisions:
                collided_component = self.get_collided_component(photon)
                if collided_component is not None:
                    # else no iteractions if no collisions
                    photon.interact_with_component(
                        collided_component, self.clock)
                self.board_displayer.add_photon_to_board(photon)
            i += 1

    def count_activated_receivers(self) -> int:
        '''
        Counts how many receivers have been activated in the circuit.

        Returns
        -------
        int
            The number of receivers that have been activated (in the current tick).
        '''
        count = 0
        i = 0
        while i < len(self.receivers):
            if self.receivers[i].is_activated():
                count += 1
            i += 1
        return count

    def run_circuit(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs the entire circuit from start to finish. This involves getting
        each emitter to emit a photon, and continuously running tick until the
        circuit is finished running. All output in regards of running the
        circuit should be contained in this method.
        '''

        start_message = '''
========================
   RUNNING CIRCUIT...
========================
'''
        print(start_message)

        self.emit_photons()  # each emitter emits a photon
        self.print_emit_photons()

        while not self.is_finished():
            self.tick()
            # print the state of the board every 5 ns or if it's the final
            # state
            if self.clock % 5 == 0 or self.is_finished():
                print(
                    f"{self.clock}ns: {self.count_activated_receivers()}/{len(self.receivers)} receiver(s) activated.")
                self.print_board()
                print()

        # finally:
        self.print_activation_times()
        self.print_total_energy()

        end_message = '''========================
   CIRCUIT FINISHED!
========================'''
        print(end_message)

    def add_emitter(self, emitter: Emitter) -> bool:
        '''
        If emitter is not an Emitter instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The emitter's position is within the bounds of the circuit.
          2)  The emitter's position is not already taken by another emitter in
              the circuit.
          3)  The emitter's symbol is not already taken by another emitter in
              the circuit.

        If at any point a check is not passed, an error message is printed
        stating the causeof the error and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur:
          1)  emitter is added in the circuit's list of emitters. emitter
              needs to be added such that the list of emitters remains sorted
              in alphabetical order by the emitter's symbol. You can assume the
              list of emitters is already sorted before you add the emitter.
          2)  emitter's symbol is added into board_displayer.
          3)  The method returns True.

        Paramaters
        ----------
        emitter - the emitter to add into this circuit's list of emitters

        Returns
        ----------
        Returns true if all checks are passed and the emitter is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter method to check for position collision.
        You will need to find your own way to check for symbol collisions
        with other emitters.
        '''
        if not isinstance(emitter, Emitter):
            return False  # premature return

        else:  # proceed with checks:
            # check indexing: x∈[0,w], y∈[0,h]
            if emitter.x < 0 or emitter.x >= self.width or emitter.y < 0 or emitter.y >= self.height:
                print(
                    f"Error: position ({emitter.x}, {emitter.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
                return False

            # ∃(collision) ⇒ emitter is "bad"
            incumbent_emitter = self.get_collided_emitter(emitter)
            if incumbent_emitter is not None:
                print(
                    f"Error: position ({emitter.x}, {emitter.y}) is already taken by emitter '{incumbent_emitter.symbol}'")
                return False

            # check if emitter symbol is new
            i = 0
            while i < len(self.emitters):
                if self.emitters[i].symbol == emitter.symbol:
                    print(f"Error: symbol '{emitter.symbol}' is already taken")
                    return False
                i += 1

        # Only run below if all checks passed
        self.emitters.append(emitter)  # causes mutation

        # Sorting to alphabetical order:
        sorter.sort_emitters_by_symbol(self.emitters)  # causes mutation

        # add emitter's symbol to board_displayer.
        self.board_displayer.add_component_to_board(emitter)

        return True  # termination

    def get_emitters(self) -> list[Emitter]:
        '''Returns emitters.'''
        sorted_emitters = sorter.sort_emitters_by_symbol(
            self.emitters)  # ensure emitters is always sorted alphabetically when needed to be used.
        return sorted_emitters

    def add_receiver(self, receiver: Receiver) -> bool:
        '''
        If receiver is not a Receiver instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The receiver's position is within the bounds of the circuit.
          2)  The receiver's position is not already taken by another emitter
              or receiver in the circuit.
          3)  The receiver's symbol is not already taken by another receiver in
              the circuit.

        If at any point a check is not passed, an error message is printed stating
        the cause of the error and returns False, skipping any further checks. If
        all checks pass, then the following needs to occur:
          1)  receiver is added in the circuit's list of receivers. receiver
              needs to be added such that the list of receivers  remains sorted
              in alphabetical order by the receiver's symbol. You can assume the
              list of receivers is already sorted before you add the receiver.
          2)  receiver's symbol is added into board_displayer.
          3)  The method returns True.

        Paramaters
        ----------
        receiver - the receiver to add into this circuit's list of receivers

        Returns
        ----------
        Returns true if all checks are passed and the receiver is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter and get_collided_receiver methods to
        check for position collisions.
        You will need to find your own way to check for symbol collisions
        with other receivers.
        '''
        if not isinstance(receiver, Receiver):
            return False  # premature return

        else:  # proceed with checks:
            # check indexing: x∈[0,w], y∈[0,h]
            if receiver.x < 0 or receiver.x >= self.width or receiver.y < 0 or receiver.y >= self.height:
                print(
                    f"Error: position ({receiver.x}, {receiver.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
                return False

            # check if position is already occupied by an emitter
            incumbent_emitter = self.get_collided_emitter(receiver)
            if incumbent_emitter is not None:
                print(
                    f"Error: position ({receiver.x}, {receiver.y}) is already taken by emitter '{incumbent_emitter.symbol}'")
                return False

            # same check for receiver
            incumbent_receiver = self.get_collided_receiver(receiver)
            if incumbent_receiver is not None:
                print(
                    f"Error: position ({receiver.x}, {receiver.y}) is already taken by receiver '{incumbent_receiver.symbol}'")
                return False

            # check if receiver symbol is new
            i = 0
            while i < len(self.receivers):
                if self.receivers[i].symbol == receiver.symbol:
                    print(
                        f"Error: symbol '{receiver.symbol}' is already taken")
                    return False
                i += 1

        # Only run below if all checks passed
        self.receivers.append(receiver)

        # Sorting to alphabetical order:
        sorter.sort_receivers_by_symbol(self.receivers)

        # add receiver's symbol to board_displayer.
        self.board_displayer.add_component_to_board(receiver)

        return True  # termination

    def get_receivers(self) -> list[Receiver]:
        '''Returns receivers.'''
        sorted_receivers = sorter.sort_receivers_by_symbol(self.receivers)
        return sorted_receivers

    def add_photon(self, photon: Photon) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        If the photon passed in is not a Photon instance, it does not add it in
        and returns False. Else, it adds photon in this circuit's list of
        photons and returns True.

        Paramaters
        ----------
        photon - the photon to add into this circuit's list of photons

        Returns
        -------
        Returns True if the photon is added in, else False.
        '''
        if not isinstance(photon, Photon):
            return False
        # will only run if conditional above is false:
        self.photons.append(photon)
        return True

    def get_photons(self) -> list[Photon]:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns photons.'''
        return self.photons

    def add_mirror(self, mirror: Mirror) -> bool:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        If mirror is not a Mirror instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The mirror's position is within the bounds of the circuit.
          2)  The mirror's position is not already taken by another emitter,
              receiver or mirror in the circuit.

        If at any point a check is not passed, an error message is printed
        stating the cause of theerror and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur:
          1)  mirror is added in the circuit's list of mirrors.
          2) mirror's symbol is added into board_displayer.
          3)   The method returns True.

        Paramaters
        ----------
        mirror - the mirror to add into this circuit's list of mirrors

        Returns
        ----------
        Returns true if all checks are passed and the mirror is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.
        '''
        if not isinstance(mirror, Mirror):
            return False

        # check if mirror's position is within the bounds of the circuit
        if mirror.x < 0 or mirror.x >= self.width or mirror.y < 0 or mirror.y >= self.height:
            print(
                f"Error: position ({mirror.x}, {mirror.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
            return False

        # check if the mirror's position is already occupied by an emitter,
        # receiver, or mirror:
        incumbent_emitter = self.get_collided_emitter(mirror)
        incumbent_receiver = self.get_collided_receiver(mirror)
        incumbent_mirror = self.get_collided_mirror(mirror)
        if incumbent_emitter is not None:
            print(
                f"Error: position ({mirror.x}, {mirror.y}) is already taken by emitter '{incumbent_emitter.get_symbol()}'")
            return False
        if incumbent_receiver is not None:
            print(
                f"Error: position ({mirror.x}, {mirror.y}) is already taken by receiver '{incumbent_receiver.get_symbol()}'")
            return False
        if incumbent_mirror is not None:
            print(
                f"Error: position ({mirror.x}, {mirror.y}) is already taken by mirror '{incumbent_mirror.get_symbol()}'")
            return False

        # all checks passed -> add the mirror
        self.mirrors.append(mirror)
        self.board_displayer.add_component_to_board(mirror)
        return True  # termination

    def get_mirrors(self) -> list[Mirror]:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns mirrors.'''
        return self.mirrors

    def get_width(self) -> int:
        '''Returns width.'''
        return self.width

    def get_height(self) -> int:
        '''Returns height.'''
        return self.height

