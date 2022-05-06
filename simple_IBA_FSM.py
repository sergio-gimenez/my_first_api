from transitions import Machine


class Intent:

    def __init__(self, verb, action, resource, context):
        self.verb = verb
        self.action = action
        self.resource = resource
        self.context = context  # TODO In general, context is an array of Context objects


'''
Define valid intents
'''


# create
# configure [?] (might be abstracted when creating a slice)
verbs = ["create", "configure"]

# slice (for verb=create)
# rina_slice (for verb=create) [?] (can this be abstracted when creating a slice, just inferred from the context? E.g., for an intent like “create slice for disaggregated_5g_core“
# hardware (for verb=configure) [?] (might be abstracted when creating a slice)
resource = ["slice", "RINA_slice", "hardware"]

# between: [node_1, …, node_n] (for verb=slice)
# for: multimedia | etc … (for verb=slice)
# with: … [?] may be useful for other types of metadata
context = ["between", "for"]
# context = ["between", "for", "with"]

'''
Define Callback Functions
'''


def say_hello(name):
    print("Hello, new state !")


def say_goodbye():
    print("Goodbye, new state!")


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
    {'trigger': 'get_action_from_intent', 'source': 'empty_intent', 'dest': 'action_given'}
]


def main():
    intent = Intent("create", "slice", "hardware", "between")

    machine = Machine(model=intent,
                      states=states,
                      transitions=transitions,
                      initial='empty_intent')

    machine.add_states(states)
    machine.add_transitions(transitions)

    import pdb
    pdb.set_trace()


if __name__ == "__main__":
    main()
