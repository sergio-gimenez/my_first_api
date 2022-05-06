from transitions import Machine


class IBFSM:

    # class Intent:

    #     '''
    #     Define valid intents
    #     '''

    #     # create
    #     # configure [?] (might be abstracted when creating a slice)
    #     verbs = ["create", "configure"]

    #     # slice (for verb=create)
    #     # rina_slice (for verb=create) [?] (can this be abstracted when creating a slice, just inferred from the context? E.g., for an intent like “create slice for disaggregated_5g_core“
    #     # hardware (for verb=configure) [?] (might be abstracted when creating a slice)
    #     resource = ["slice", "RINA_slice", "hardware"]

    #     # between: [node_1, …, node_n] (for verb=slice)
    #     # for: multimedia | etc … (for verb=slice)
    #     # with: … [?] may be useful for other types of metadata
    #     context = ["between", "for"]
    #     # context = ["between", "for", "with"]

    #     '''
    #     Define Callback Functions
    #     '''

    #     def say_hello():
    #         print("Hello, new state !")

    #     def say_goodbye():
    #         print("Goodbye, new state!")

    #     def __init__(self, verb, action, resource, context):
    #         # TODO add checking for valid intents
    #         self.verb = verb
    #         self.action = action
    #         self.resource = resource
    #         self.context = context  # TODO In general, context is an array of Context objects

    '''
    Define States
    '''
    states = [
        {'name': 'empty_intent', 'on_exit': ['say_goodbye']},
        'action_given',
        'resource_given',
        'ctxt_given',
        'invalid'
    ]

    '''
    Define transitions between states
    '''

    transitions = [
        {'trigger': 'got_verb_from_intent', 'source': 'empty_intent', 'dest': 'action_given'},
        {'trigger': 'got_invalid_verb_from_intent', 'source': 'empty_intent', 'dest': 'invalid'},

        {'trigger': 'got_action_from_intent', 'source': 'action_given', 'dest': 'resource_given'},
        {'trigger': 'got_invalid_action_from_intent', 'source': 'action_given', 'dest': 'invalid'},

        # TODO add conditions in resources and context transactions
        {'trigger': 'got_resource_from_intent', 'source': 'resource_given', 'dest': 'ctxt_given'},
        
        {'trigger': 'got_ctxt_from_intent', 'source': 'ctxt_given', 'dest': 'ctxt_given'},
    ]

    def __init__(self, model):

        self.fsm = Machine(model=model,
                           states=IBFSM.states,
                           transitions=IBFSM.transitions,
                           initial='empty_intent')

        # machine.add_states(IBFSM.states)
        # machine.add_transitions(IBFSM.transitions)
