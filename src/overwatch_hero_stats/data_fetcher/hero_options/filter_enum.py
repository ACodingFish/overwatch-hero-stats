from enum import Enum

class FilterEnum(Enum):
    def __new__(cls): # Auto Numbering for members
        curr_index = len(cls.__members__)
        obj = object.__new__(cls)
        obj._value_ = curr_index
        return obj

    @classmethod
    def default(cls):
        return cls(0)
    
    # Ex. For state switching:
    #     self.map = self.map.get_state_at_index(3)
    @classmethod
    def get_state_at_index(self, index:int):
        if (index < len(self.__members__)):
            return self(index)

    
    def value_name(self):
        return self.name.replace("-","_")
    
    def value_param(self):
        if hasattr(self, "use_idx_4_param") and self.use_idx_4_param == True:
            return str(self.value)
        else:
            return self.value_name()
    
    def filter_name(self):
        return self.filter_str if hasattr(self, "filter_str") else "Unknown"
    

def merge_enums(filter_name, name, enum_list) -> FilterEnum:
    combined_members = {}
    for single_enum in enum_list:
        for member in single_enum.__members__:
            if member not in combined_members:
                combined_members[member] = ()
    new_filter = FilterEnum(name, combined_members)
    new_filter.filter_str = filter_name
    return new_filter