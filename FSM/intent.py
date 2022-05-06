class Intent:

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

    def received_action_cb(self):
        print("Hello, new state !")

    def received_resource_cb(self):
        print("Goodbye, new state!")

    def __init__(self, verb, action, resource, context):
        # TODO add checking for valid intents
        self.verb = verb
        self.action = action
        self.resource = resource
        self.context = context  # TODO In general, context is an array of Context objects
