"""
    Created on Jan 12 2026

    Description: Library of useful recipes for the SPECTRUM pipeline

    @author: Eder Martioli <emartioli@lna.br>

    Laboratório Nacional de Astrofísica - LNA/MCTI
    """

import logging


def start_logger(file_name="") :

    """ Pipeline function to start logger
    Parameters
    ----------
    file_name : str
        define output logger file name

    Returns
    -------
    logger : Logger object
    
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    #stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    if file_name != "" :
        file_handler = logging.FileHandler(file_name)
        #file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
