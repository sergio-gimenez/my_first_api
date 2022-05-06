from intent import Intent
from fsm import IBFSM
import pdb


def main():

    print("Given intent: Create slice for holoconference purposes between node_x and node_y")
    intent = Intent("create", "slice", ["node_x", "node_y"])
    print("Parsed " + str(intent))
    IBFSM(intent)
    pdb.set_trace()


if __name__ == "__main__":
    main()
