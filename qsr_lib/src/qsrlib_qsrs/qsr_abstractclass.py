# -*- coding: utf-8 -*-
from __future__ import print_function, division
from abc import ABCMeta, abstractmethod
import yaml
import os


class QSR_Abstractclass(object):
    """Abstract class for the QSR makers"""
    __metaclass__ = ABCMeta

    def __init__(self):
        self._unique_id = ""  # must be the same that goes in the QSRlib.__qsrs_registration
        self.all_possible_relations = []
        self._allowed_parameters = ["qsrs_for"]
        self._dtype = ""

    @abstractmethod
    def make_world_qsr_trace(self, world_trace, timestamps, qsr_params, req_params, **kwargs):
        """The main function that makes the returned World_QSR_Trace and each QSR has to implement.

        :param world_trace:
        :param timestamps:
        :param qsr_params:
        :param dynamic_args:
        :param kwargs:
        :return:
        """
        return

    @abstractmethod
    def _init_qsrs_for_default(self, objects_names_of_world_state, **kwargs):
        """The default list of entities at each time-step (i.e. World_State.objects.keys() for which QSRs are computed for.

        Usually this is provided by a parent class and there is no need for the QSRs to implement it, unless they want
        to override the parent default method.

        :param objects_names_of_world_state:
        :param req_params:
        :param kwargs:
        :return:
        """
        return

    @abstractmethod
    def _validate_qsrs_for(self, qsrs_for):
        """Custom checks of the qsrs_for field.

        Usually this is provided by a parent class and there is no need for the QSRs to implement it, unless they want
        to override the parent default method.

        :param qsrs_for: list of strings and/or tuples for which QSRs will be computed
        :return: qsrs_for
        """
        return qsrs_for

    def get_qsrs(self, **req_params):
        """

        :param req_params: The request args
        :return: Computed World_QSR_Trace
        :rtype: World_QSR_Trace
        """
        world_trace, timestamps = self._set_input_world_trace(req_params["input_data"])
        qsr_params = self._process_qsr_parameters_from_request_parameters(req_params)
        world_qsr_trace = self.make_world_qsr_trace(world_trace, timestamps, qsr_params, req_params)
        world_qsr_trace = self._postprocess_world_qsr_trace(world_qsr_trace, world_trace, timestamps, qsr_params, req_params)
        return world_qsr_trace

    def custom_checks(self, input_data):
        # todo needs to be refactored to a better name; not even sure if needed or should be integrated somewhere else
        """Customs checks on the input data.

        :param input_data:
        :return:
        """
        return 0, ""

    # todo can be simplified a bit, also custom_checks possibly not needed anymore here
    def _set_input_world_trace(self, world_trace):
        error_code, error_msg = self.custom_checks(input_data=world_trace)
        if error_code > 0:
            raise RuntimeError("Something wrong with the input data", error_code, error_msg)
        timestamps = world_trace.get_sorted_timestamps()
        return world_trace, timestamps

    def _process_qsrs_for(self, objects_names, dynamic_args, **kwargs):
        if isinstance(objects_names[0], str):
            try:
                return self.__check_qsrs_for_data_exist_at_world_state(objects_names,
                                                                       dynamic_args[self._unique_id]["qsrs_for"])
            except KeyError:
                try:
                    return self.__check_qsrs_for_data_exist_at_world_state(objects_names,
                                                                           dynamic_args["for_all_qsrs"]["qsrs_for"])
                except KeyError:
                    return self._init_qsrs_for_default(objects_names)
        elif isinstance(objects_names[0], (list, tuple)):
            qsrs_for_list = []
            for objects_names_i in objects_names:
                try:
                    qsrs_for_list.append(self.__check_qsrs_for_data_exist_at_world_state(objects_names_i,
                                                                                         dynamic_args[self._unique_id]["qsrs_for"]))
                except KeyError:
                    try:
                        qsrs_for_list.append(self.__check_qsrs_for_data_exist_at_world_state(objects_names_i,
                                                                                             dynamic_args["for_all_qsrs"]["qsrs_for"]))
                    except KeyError:
                        qsrs_for_list.append(self._init_qsrs_for_default(objects_names_i))

            return list(set(qsrs_for_list[0]).intersection(*qsrs_for_list))
        else:
            raise TypeError("objects_names must be a list of str or list of lists")

    def __check_qsrs_for_data_exist_at_world_state(self, objects_names_of_world_state, qsrs_for):
        if len(objects_names_of_world_state) == 0:
            return []
        if not isinstance(qsrs_for, (list, tuple)):
            raise TypeError("qsrs_for must be list or tuple")
        qsrs_for_ret = []
        for p in qsrs_for:
            if isinstance(p, str):
                if p in objects_names_of_world_state:
                    qsrs_for_ret.append(p)
            elif isinstance(p, (list, tuple)):
                tuple_data_exists = True
                for o in p:
                    if o not in objects_names_of_world_state:
                        tuple_data_exists = False
                        break
                if tuple_data_exists:
                    qsrs_for_ret.append(p)
            else:
                raise TypeError("Elements of qsrs_for must be strings and/or tuples")
        qsrs_for_ret = self._validate_qsrs_for(qsrs_for_ret)
        return qsrs_for_ret

    def _process_qsr_parameters_from_request_parameters(self, req_params, **kwargs):
        """

        Overwrite as needed.

        :param req_params:
        :param kwargs:
        :return:
        """
        return {}

    def _postprocess_world_qsr_trace(self, world_qsr_trace, world_trace, world_trace_timestamps, qsr_params, req_params, **kwargs):
        """

        Overwrite as needed.

        :param world_qsr_trace:
        :param world_trace:
        :param world_trace_timestamps:
        :param qsr_params:
        :return:
        """
        return world_qsr_trace

    def _set_from_config_file(self, path):
        try:
            import rospkg
        except ImportError:
            raise ImportError("Module rospkg not found; setting from config file works for now only within the ROS eco-system")
        if path is None:
            path = os.path.join(rospkg.RosPack().get_path("qsr_lib"), "cfg/defaults.yml")
        else:
            path_ext = os.path.splitext(path)[1]
            if path_ext != ".yml" and path_ext != ".yaml":
                print("ERROR (qsr_abstractclass.py/set_from_config_file): Only yaml files are supported")
                raise ValueError
        with open(path, "r") as f:
            document = yaml.load(f)
        self._custom_set_from_config_file(document)

    def _custom_set_from_config_file(self, document):
        """

        Overwrite as needed.

        :param document:
        :return:
        """
        raise NotImplemented(self._unique_id, "has no support from reading from config file")

    def _format_qsr(self, v):
        return {self._unique_id: v}
