from turing_machine import TuringMachine


delta_funcs = (
    ((0,"0"), (1, "0", "R")),
    ((1,"0"), (0, "0", "R")),
    ((0,"1"), (0, "1", "R")),
    ((0," "), (2, " ", "-"))
)

initial_state = 0

accepting_state = 2


tm = TuringMachine(delta_funcs, initial_state, accepting_state)

tm.run("10011")
