import unittest
from intent import Intent
from fsm import IBFSM


class TestFSM(unittest.TestCase):

    # Test FSM initialization
    def test_initialization(self):
        intent = Intent("create", "slice", "hardware")
        IBFSM(intent)

        self.assertEqual(intent.state, "empty_intent", "Should be empty_intent")

    # Test "First level" FSM transitions
    def test_first_line(self):
        intent = Intent("create", "slice", "hardware")
        IBFSM(intent)

        intent.got_action_from_intent()
        self.assertEqual(intent.state, "action_given", "Should be action_given")

        intent.got_resource_from_intent()
        self.assertEqual(intent.state, "resource_given", "Should be resource_given")

        intent.got_ctxt_from_intent()
        self.assertEqual(intent.state, "ctxt_given", "Should be ctxt_given")

        intent.got_ctxt_from_intent()
        self.assertEqual(intent.state, "ctxt_given", "Should be ctxt_given")


if __name__ == '__main__':
    unittest.main()
