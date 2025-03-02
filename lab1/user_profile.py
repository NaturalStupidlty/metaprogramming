from managed_attribute import ManagedAttribute
from structure_fixer import StructureFixer
from logging_managed_attribute import attr_change_logger


@attr_change_logger
class UserProfile(metaclass=StructureFixer):
    __allow_dynamic_changes__ = False

    name = ManagedAttribute()
    age = ManagedAttribute()
    email = ManagedAttribute()
    password = ManagedAttribute()
    personal_code = ManagedAttribute()

    def __init__(self, name, age, email, password, personal_code):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.personal_code = personal_code
