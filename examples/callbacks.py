import pdb
from transitions import Machine, State


class Matter(object):
    def make_hissing_noises(self): print("HISSSSSSSSSSSSSSSS")
    def disappear(self): print("where'd all the liquid go?")


states = [
    State(name='solid'),
    'liquid',
    {'name': 'gas'}
]

transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid', 'before': 'make_hissing_noises'},
    {'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas', 'after': 'disappear'}
]

lump = Matter()
machine = Machine(lump, states, transitions=transitions, initial='solid')

pdb.set_trace()

lump.melt()
lump.evaporate()
