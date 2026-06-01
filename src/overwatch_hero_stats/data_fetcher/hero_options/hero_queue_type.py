from .filter_enum import FilterEnum

class HeroQueueType(FilterEnum):
    def __init__(self):
        self.filter_str = "rq"
        self.use_idx_4_param=True

    QP_Role_Queue=()
    RESERVED_1=()
    COMP_Role_Queue=()
