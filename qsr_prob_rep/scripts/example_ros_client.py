#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qsrrep_ros.ros_client import ROSClient
from qsrrep_lib.rep_io import HMMRepRequestCreate, HMMRepRequestSample, HMMRepRequestLogLikelihood
from qsrrep_lib.rep_lib import ProbRepLib
import os
import rospy
import json
import argparse

def load_files(path):
    ret = []
    for f in os.listdir(path):
        if f.endswith(".qsr"):
            filename = path + '/' + f
            with open(filename, 'r') as qsr:
                ret.append(json.load(qsr))

    return ret


if __name__ == "__main__":

    # General parsers
    general = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,add_help=False)
    parser = argparse.ArgumentParser(parents=[general])
    subparsers = parser.add_subparsers(dest='action')
    qtc_parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,add_help=False)
    qtc_parse.add_argument('-qsr', '--qsr_type', help="choose qsr: %s" % ProbRepLib.hmm_types_available.keys(), type=str, required=True)

    # Parsers for create function
    create_parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,add_help=False)
    create_parse.add_argument('-i', '--input', help="reads *.qsr files from the given directory", type=str, required=True)
    create_parse.add_argument('-o', '--output', help="the file to which to write the resulting xml", type=str, required=True)
    subparsers.add_parser('create',parents=[general, qtc_parse, create_parse])

    # Parsers for sample function
    sample_parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,add_help=False)
    sample_parse.add_argument('-i', '--input', help="the xml file containing the HMM", type=str, required=True)
    sample_parse.add_argument('-o', '--output', help="the file to which to write the resulting samples", type=str)
    sample_parse.add_argument('-n', '--num_samples', help="the number of samples to take", type=str, required=True)
    sample_parse.add_argument('-l', '--max_length', help="the maximum length of samples which will be ensure if at all possible", type=str, required=True)
    subparsers.add_parser('sample', parents=[general, sample_parse, qtc_parse])

    # Parsers for loglikelihood function
    log_parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,add_help=False)
    log_parse.add_argument('-i', '--input', help="the xml file containing the HMM", type=str, required=True)
    log_parse.add_argument('-q', '--qsr_seq', help="reads a file containing state chains", type=str, required=True)
    subparsers.add_parser('loglikelihood', parents=[general, log_parse, qtc_parse])

    # Parse arguments
    args = parser.parse_args()

    rospy.init_node("ros_client")
    r = ROSClient()

    if args.action == "create":
        qsr_seq = load_files(args.input)
        q, d = r.call_service(
            HMMRepRequestCreate(
                qsr_seq=qsr_seq,
                qsr_type=args.qsr_type
            )
        )
        with open(args.output, 'w') as f: f.write(d)

    elif args.action == "sample":
        with open(args.input, 'r') as f: hmm = f.read()
        q, s = r.call_service(
            HMMRepRequestSample(
                qsr_type=args.qsr_type,
                xml=hmm,
                max_length=args.max_length,
                num_samples=args.num_samples
            )
        )
        try:
            with open(args.output, 'w') as f: json.dump(s, f)
        except TypeError:
            print s

    elif args.action == "loglikelihood":
        with open(args.qsr_seq, 'r') as f: qsr_seq = json.load(f)
        with open(args.input, 'r') as f: hmm = f.read()
        q, l = r.call_service(
            HMMRepRequestLogLikelihood(
                qsr_type=args.qsr_type,
                xml=hmm,
                qsr_seq=qsr_seq
            )
        )
        print l
