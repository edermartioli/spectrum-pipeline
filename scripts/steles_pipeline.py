"""
    Created on Jan 12 2026

    Description: Pipeline to process STELES data using the SPECTRUM pipeline

    @author: Eder Martioli <martioli@lna.br>

    Laboratório Nacional de Astrofísica - LNA/MCTI

    Simple usage examples:

    python -W"ignore" ~/spectrum-pipeline/scripts/steles_pipeline.py
    """

import glob
import os, sys
from optparse import OptionParser

import espectro.params as params
import espectro.pipeline_lib as spcpipelib
import espectro.product_plots as spcplt

parser = OptionParser()
parser.add_option("-r", "--reducedir", dest="reducedir", help="Reduced data directory", type='string', default="./")
parser.add_option("-c", "--calibdbdir", dest="calibdbdir", help="Calibration data directory", type='string', default="")
parser.add_option("-b", "--bias", dest="bias", help="wildcard for bias selection", type='string', default="")
parser.add_option("-F", "--flat", dest="flat", help="wildcard for flat selection", type='string', default="")
parser.add_option("-s", "--science", dest="science", help="wildcard for science data selection", type='string', default="")
parser.add_option("-o", "--object", dest="object", help="object id", type='string', default="unknown_object")
parser.add_option("-t", "--time_key", dest="time_key", help="time keyword", type='string', default="DATE-OBS")
parser.add_option("-a", "--ra", dest="ra", help="RA", type='string', default="")
parser.add_option("-d", "--dec", dest="dec", help="Dec", type='string', default="")
parser.add_option("-m", "--params", dest="params",help="Input parameters yaml file",type='string',default="")
parser.add_option("-f", action="store_true", dest="force", help="Force reduction", default=False)
parser.add_option("-p", action="store_true", dest="plot", help="plot", default=False)
parser.add_option("-v", action="store_true", dest="verbose", help="verbose", default=False)

try:
    options, args = parser.parse_args(sys.argv[1:])
except:
    print("Error: check usage with -h steles_pipeline.py")
    sys.exit(1)

# load pipeline parameters
p = params.load_spectrum_parameters()
