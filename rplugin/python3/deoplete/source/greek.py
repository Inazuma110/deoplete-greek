from .base import Base
from deoplete.util import load_external_module
load_external_module(__file__, 'source')
from data import GREEK_DICT

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'greek'
        self.mark = '[greek]'
        self.min_pattern_length = 1

    def gather_candidates(self, context):
        return [{'word': k, 'kind': '{}'.format(v)} for (k, v) in GREEK_DICT.items()]
