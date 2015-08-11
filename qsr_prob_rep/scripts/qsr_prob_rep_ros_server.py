#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import json
from qsrrep_lib.rep_lib import ProbRepLib
# Wildard import necessary because I don't know which services exist, they are defined in 'qsrrep_lib.rep_io.available_services'
from qsrrep_lib.rep_io import *
from qsr_prob_rep.srv import QSRProbRepResponse, QSRProbRep


class HMMRepROSServer(object):
    """This class provides a service for all requests specified in
    'qsrrep_lib.rep_io.available_services'. The service name will be the key
    of the entry."""

    def __init__(self, name):
        """
        :param name: The name of the node
        """
        rospy.loginfo("Starting %s" % name)
        self._hmm_lib = ProbRepLib()
        self._hmm_lib.print_hmms_available()
        self.services = {}
        # Automatically creating a service for all the entries in 'qsrrep_lib.rep_io.available_services'
        # Passing the key of the dict entry to the service to identify the right function to call
        for i, k in enumerate(available_services.keys()):
            # The outer lambda function creates a new scope for the inner lambda function
            # This is necessary to preserve the value of k, otherwise it will have the same value for all services
            # x will be substituded by the service request
            self.services[k] = rospy.Service("~"+k, QSRProbRep, (lambda b: lambda x: self.callback(x, b))(k))

    def callback(self, req, srv_type):
        r = available_services[srv_type][0](qsr_type=req.qsr_type, **json.loads(req.data))
        return QSRProbRepResponse(qsr_type=req.qsr_type, data=self._hmm_lib.request(r).get())


if __name__ == '__main__':
    rospy.init_node("prob_rep_ros_server")
    h = HMMRepROSServer(rospy.get_name())
    rospy.spin()
