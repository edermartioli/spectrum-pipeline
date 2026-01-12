"""
    Created on Jan 12 2026

    Description: Library of recipes for the SPECTRUM pipeline

    @author: Eder Martioli <emartioli@lna.br>

    Laboratório Nacional de Astrofísica - LNA/MCTI
    """

import os

import espectro.db as spcdb
import espectro.params as params
import espectro.product_plots as spcplt
import espectro.products as spcprods
import espectro.utils as spcutils
import espectro.version as spcver
import espectro.pipeline_lib as spcpipelib
 
logger = spcutils.start_logger()
