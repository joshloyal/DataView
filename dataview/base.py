from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division


from dataview import data_types as types
from dataview.wrappers import DataViewMeta, registry
import dataview.data_utils as data_utils


class DataSchema(object):
    def __init__(self):
        self._schema = {}

    @property
    def columns(self):
        return self._schema.keys()

    def analyze(self, data):
        for column in data_utils.numeric_columns(data):
            self._schema[column] = types.DataTypes.NUMERIC

        for column in data_utils.categorical_columns(data):
            self._schema[column] = types.DataTypes.CATEGORICAL

        return self

    def select(self, data_types):
        if isinstance(data_types, types.DataTypes):
            data_types = [data_types]

        return DataSchema.from_dict(
                {k: v for k, v in self._schema.iteritems() if v in data_types})


    def update_type(self, column_name, data_type):
        if not isinstance(data_type, types.DataTypes):
            raise ValueError('Must be DataType')
        self._schema[column_name] = data_type

    def to_dict(self):
        return self._schema

    @classmethod
    def from_dict(cls, data):
        new_schema = cls()
        new_schema._schema = data
        return new_schema


class DataView(object):
    """DataView

    An object to manipulate datasets.
    """
    __metaclass__ = DataViewMeta
    def __init__(self):
        self._data = None
        self._schema = None

    @property
    def schema(self):
        if self._schema is None:
            self._schema = DataSchema().analyze(self._data)

        return self._schema

    @property
    def data(self):
        return self._data.copy()

    def view(self, all_types, partition_method, pipeline):
        dv = self.select(all_types)
        for instruction in pipeline:
            if instruction[0] == types.DataTypes.ALL:
                dv.values
            instruction[2].fit_transform(self.select(intruction[0]).data.values)

    def fetch(self):
        raise NotImplementedError()

    def select(self, data_types):
        subset = self._data[self.schema.select(data_types).columns]
        return self.__class__.from_dataframe(subset)

    @classmethod
    def from_dataframe(cls, dataframe):
        new_view = cls()
        new_view._data = dataframe.copy()
        return new_view


def fetch_view(view_name):
    if view_name not in registry:
        raise ValueError('Not recognized view')
    dv = registry[view_name]()
    dv.fetch()
    return dv
