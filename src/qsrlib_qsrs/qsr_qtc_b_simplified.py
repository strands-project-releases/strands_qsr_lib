# -*- coding: utf-8 -*-
"""Example that shows how to implement QSR makers.

:Author: Christan Dondrup <cdondrup@lincoln.ac.uk>, Yiannis Gatsoulis <y.gatsoulis@leeds.ac.uk>
:Organization: University of Lincoln
:Date: 10 September 2014
:Version: 0.1
:Status: Development
:Copyright: STRANDS default
:Notes: future extension to handle polygons, to do that use matplotlib.path.Path.contains_points
        although might want to have a read on the following also...
        http://matplotlib.1069221.n5.nabble.com/How-to-properly-use-path-Path-contains-point-td40718.html
"""

from __future__ import print_function, division
from qsrlib_qsrs.qsr_qtc_simplified_abstractclass import QSR_QTC_Simplified_Abstractclass


class QSR_QTC_B_Simplified(QSR_QTC_Simplified_Abstractclass):
    """Make default QSRs and provide an example for others"""
    def __init__(self):
        super(QSR_QTC_B_Simplified, self).__init__()
        self._unique_id = "qtcbs"
        self.qtc_type = "b"
        self.all_possible_relations = self.return_all_possible_state_combinations()[0]

    def qtc_to_output_format(self, qtc):
        """Overwrite this for the different QTC veriants to select only the parts
        from the QTCC tuple that you would like to return.
        Example for QTCB: return qtc[0:2]

        :param qtc: The full QTCC tuple [q1,q2,q4,q5]

        :return: "q1,q2" of {"qtcbs": "q1,q2"} if future is True
        """
        return self._format_qsr(self.create_qtc_string(qtc[0:2]))
