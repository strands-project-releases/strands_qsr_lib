# -*- coding: utf-8 -*-
from __future__ import print_function, division
from qsrlib_qsrs.qsr_rcc_abstractclass import QSR_RCC_Abstractclass


class QSR_RCC2_Rectangle_Bounding_Boxes_2D(QSR_RCC_Abstractclass):
    """RCC2 relations.

    	# 'dc'     bb1 is disconnected from bb2
		# 'c'      bb1 is connected to bb2
    """
    def __init__(self):
        super(QSR_RCC2_Rectangle_Bounding_Boxes_2D, self).__init__()
        self._unique_id = "rcc2"
        self.all_possible_relations = ["dc", "c"]

    def _convert_to_requested_rcc_type(self, qsr):
        return qsr if qsr == "dc" else "c"
