from doubly_linked_list import DoublyLinkedList
import time

# TODO: bug check of the inputs

class TuringMachine:

    def __init__(self, delta_funcs, initial_state, accepting_state):
        # array of delta funtions
        # format: for (qi, s) -> (qj, s2, R) ((qi, s), (qj, s2, R))
        self.delta_funcs = delta_funcs

        self.initial_state = initial_state

        self.accepting_state = accepting_state

        self.input = ""

        # sets the current bit the head of the tm is pointing to
        self.current_bit = 0
        # sets the current state of the machine
        self.current_state = self.initial_state

    # runs the turing machine with the given input and returns the output
    def run(self, input_string):
        time1 = time.time()

        # convert the input to a  doubly linked list
        band = DoublyLinkedList()
        for letter in input_string:
            band.append(letter)

        tm_is_running = True

        while (tm_is_running):
            #print("current_bit ", band.get(self.current_bit))
            #print("current_state ", self.current_state)
            #print()

            # main loop
            for delta in self.delta_funcs:
                #print("delta ", delta)

                # find the delta function for the current symbol and current state
                if delta[0][0] == self.current_state and delta[0][1] == band.get(self.current_bit):
                    # set the new state
                    self.current_state = delta[1][0]
                    # set the new symbol
                    band.replace(self.current_bit, delta[1][1])
                    direction = delta[1][2]
                    if direction == "R":
                        self.current_bit += 1
                        if band.get(self.current_bit + 1) == None:
                            band.append(" ")
                    if direction == "L":
                        band.push(" ")
                        self.current_bit = 0
                    break

            # check if the current state is the accepting state
            if (self.current_state == self.accepting_state):
                tm_is_running = False
                time2 = time.time()
                print('accepted in %0.3f ms' % ((time2-time1) * 1000.0))
                return
