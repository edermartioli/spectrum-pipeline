import os
import yaml

def load_spectrum_parameters(config_file=None):
    """Load SPECTRUM pipeline parameters from a yaml file.

    Parameters
    ----------
    config_file : str (optional)
        Path to yaml file containing pipeline parameters. If None, the
        default parameters are loaded.

    Returns
    -------
    params : dict
        Dictionary containing pipeline parameters.
    """
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    spc_parent_dir = os.path.abspath(os.path.join(current_directory, os.pardir))

    if config_file is None:
        config_file = os.path.join(current_directory,'spectrum_params.yaml')
        
    with open(config_file, 'r') as f:
        params = yaml.safe_load(f)

    return params
