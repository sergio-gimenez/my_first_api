class Intent:

    '''
    Define valid intents
    '''

    # create
    # configure [?] (might be abstracted when creating a slice)
    actions = ["create", "configure"]

    # slice (for verb=create)
    # rina_slice (for verb=create) [?]
    #  (can this be abstracted when creating a slice, just inferred
    # from the context?  E.g., for an intent like
    #  “create slice for disaggregated_5g_core“
    # hardware (for verb=configure) [?]
    # (might be abstracted when creating a slice)
    resources = ["slice", "RINA_slice", "hardware"]

    # between: [node_1, …, node_n] (for verb=slice)
    # for: multimedia | etc … (for verb=slice)
    # with: … [?] may be useful for other types of metadata
    contexts = ["between", "for"]
    # context = ["between", "for", "with"]

    '''
    Define Callback Functions
    '''

    def received_action_cb(self):
        print("Received an valid action")

    def received_resource_cb(self):
        print("Received a valid resource")

    def received_context_cb(self):
        print("Received a valid context")

    def __init__(self, action, resource, context):
        # TODO add checking for valid intents
        self.action = action

        # TODO In general, context is an array of Context objects
        self.resource = resource
        self.context = context

    def __str__(self):
        return "Intent = [Action={0}, Resource={1}, Context={2}]".format(self.action, self.resource, self.context)
