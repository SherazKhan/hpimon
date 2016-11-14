# -*- coding: utf-8 -*-
"""
Talk directly to MEG system / read acquisition config files.

@author: jussi (jnu@iki.fi)

"""

import os.path as op

COLLECTOR_CONF = '/neuro/dacq/setup/collector/conf/collector.defs'


def read_collector_config():
    """ Read parameters from collector setup file. """
    hpifreqs = []
    linefreq = None
    if op.isfile(COLLECTOR_CONF):
        with open(COLLECTOR_CONF, 'r') as f:
            flines = f.read().splitlines()
        for line in flines:
            lit = line.split()
            if len(lit) > 1:
                if lit[0].find('hpiFreq') == 0:
                    hpifreqs.append(float(lit[1]))
                elif lit[0].find('lineFreq') == 0:
                    linefreq = float(lit[1])
    return linefreq, hpifreqs
