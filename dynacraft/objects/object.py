import copy


class Object:
    def __init__(self, fields=None, types=None, keyType=None, objType=None):
        self.types = types if types is not None else ["object"]
        self.keyType = keyType if keyType is not None else ["object"]
        self.objType = objType if objType is not None else ["object"]
        self.private_fields = {}
        self.public_fields = {}
        self.fields = fields if fields is not None else {}
        self.fields_per_type = {}  # Initialize as empty dictionary
        self.set_initial_fields(fields)

    def set_initial_fields(self, fields):
        if fields:
            for key, val in fields.items():
                self.set_public_field(key, val)
                self._track_field(key, "public")

    def set_private_field(self, key, value):
        self.private_fields[key] = value
        self._track_field(key, "private")

    def get_private_field(self, key):
        return self.private_fields.get(key, None)

    def get_public_field(self, key):
        return self.public_fields.get(key, None)

    def get_private_set(self):
        return self.private_fields

    def set_public_field(self, key, value):
        self.public_fields[key] = value
        self._track_field(key, "public")

    def add_public_field(self, key, value):
        if key not in self.public_fields:
            self.public_fields[key] = []
        self.public_fields[key].append(value)

    def set_initial_field(self, key, value):
        self.fields[key] = value

    def get_public_field(self, key):
        return self.public_fields.get(key, None)

    def get_initial_field(self, key):
        return self.fields.get(key, None)

    def get_public_set(self):
        return self.public_fields

    def get_all_fields(self):
        all_fields = {
            'types': self.types,
            'initial_fields': self.fields,
            'public_fields': self.public_fields,
            'private_fields': self.private_fields
        }
        return all_fields

    def make_field_private(self, key):
        if key in self.public_fields:
            value = self.public_fields.pop(key)
            self.set_private_field(key, value)
            self._update_field_tracking(key, "public", "private")
        else:
            raise KeyError(f"{key} not found in public fields")

    def make_field_public(self, key):
        if key in self.private_fields:
            value = self.private_fields.pop(key)
            self.set_public_field(key, value)
            self._update_field_tracking(key, "private", "public")
        else:
            raise KeyError(f"{key} not found in private fields")

    def _track_field(self, key, field_type):
        current_type = self.types[-1] if self.types else "object"
        if current_type not in self.fields_per_type:
            self.fields_per_type[current_type] = {"public": set(), "private": set()}
        self.fields_per_type[current_type][field_type].add(key)

    def _update_field_tracking(self, key, from_type, to_type):
        for field_type, fields in self.fields_per_type.items():
            if key in fields[from_type]:
                fields[from_type].remove(key)
                fields[to_type].add(key)

    def is_empty(self):
        return not self.private_fields and not self.public_fields

    def copy(self):
        new_obj = Object(
            fields=copy.deepcopy(self.fields),
            types=copy.deepcopy(self.types)
        )
        new_obj.private_fields = copy.deepcopy(self.private_fields)
        new_obj.public_fields = copy.deepcopy(self.public_fields)
        return new_obj

    def __getattr__(self, name, use_default=False):
        if use_default:
            return super().__getattr__(name)
        else:
            if name in self.public_fields:
                return self.public_fields[name]
            if name in self.private_fields:
                return self.private_fields[name]
            elif name in self.fields:
                return self.fields[name]
            raise AttributeError(f"{name} not found in public, private fields, or initial fields")

    def __str__(self):
        return f"Object with types {self.types}, public fields {self.public_fields}, private fields {self.private_fields}, keyType {self.keyType}, objType {self.objType}"

    def __repr__(self):
        return f"Object with types {self.types}, public fields {self.public_fields}, private fields {self.private_fields}, keyType {self.keyType}, objType {self.objType}"


class BoolObject(Object):
    def __init__(self, bool_value):
        super().__init__(fields={"value": bool_value}, types=["object", "bool"])


def my_int(value):
    self = object()
    self.data = value
    return self


def my_float(value):
    self = object()
    self.data = value
    return self