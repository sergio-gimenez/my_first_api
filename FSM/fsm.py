from transitions import Machine


class IBFSM:

    """
    Define States
    """
    states = [
        {"name": "empty_intent", "on_exit": ["received_action_cb"]},
        {"name": "action_given", "on_exit": ["received_resource_cb"]},
        {"name": "resource_given", "on_exit": ["received_context_cb"]},
        {"name": "ctxt_given", "on_exit": ["received_context_cb"]},
        "invalid"
    ]

    """
    Define transitions between states
    """

    transitions = [
        {
            "trigger": "got_action_from_intent",
            "source": "empty_intent",
            "dest": "action_given"
        },
        {
            "trigger": "got_invalid_action_from_intent",
            "source": "empty_intent", "dest": "invalid"
        },
        {
            "trigger": "got_resource_from_intent",
            "source": "action_given",
            "dest": "resource_given"
        },
        {
            "trigger": "got_invalid_resource_from_intent",
            "source": "action_given",
            "dest": "invalid"
        },
        # TODO add conditions in resources and context transactions
        {
            "trigger": "got_ctxt_from_intent",
            "source": "resource_given",
            "dest": "ctxt_given"
        },
        {
            "trigger": "got_ctxt_from_intent",
            "source": "ctxt_given",
            "dest": "ctxt_given"
        },

    ]

    def __init__(self, model):

        self.fsm = Machine(model=model,
                           states=IBFSM.states,
                           transitions=IBFSM.transitions,
                           initial="empty_intent")
