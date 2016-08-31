from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

import pandas as pd

from dataview import DataView
import dataview.dv_io as io
import dataview.exceptions as ex


class DiabetesView(DataView):
    def fetch(self):
        try:
            self._data = pd.read_csv(io.file_location('10k_diabetes.csv'))
        except IOError:
            raise ex.DatasetNotFound('Could not locate `10k_diabetes.csv`.')

        return self._data
