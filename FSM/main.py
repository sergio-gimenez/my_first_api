from intent import Intent
from fsm import IBFSM


def main():

    # intent = Intent("create", "slice", "hardware", "amarisoft", "between", "A", "B")
    intent = Intent("create", "slice", "hardware")
    print(intent)
    intent_fsm = IBFSM(intent)

    import pdb
    pdb.set_trace()


if __name__ == "__main__":
    main()
