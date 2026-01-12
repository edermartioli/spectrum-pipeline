![Alt text](Figures/spectrum-pipeline-logo.png?raw=true "Title")
# spectrum-pipeline

`spectrum-pipeline` is a set of routines designed to reduce long-slit and échelle spectroscopic data obtained with the [ECHARPE](https://ui.adsabs.harvard.edu/abs/2012SPIE.8446E..36D/abstract) instrument installed at the [Pico dos Dias Observatory (OPD/LNA)](https://www.gov.br/lna/pt-br/composicao-1/coast/obs/opd) and with the [STELES](https://noirlab.edu/public/programs/ctio/soar-telescope/steles/) instrument installed at the [SOAR Telescope](https://noirlab.edu/public/programs/ctio/soar-telescope/). The pipeline provides a main execution module—`echarpe_pipeline.py` or `steles_pipeline.py`—which can be run from the command line to automatically reduce data from the two spectral channels. 
Configuration of the reduction process is handled through the `spectrum_params.yaml` file, which defines the execution parameters and allows the user to tailor the reduction settings to specific scientific requirements.

# Installation

```
git clone https://github.com/edermartioli/spectrum-pipeline.git

cd spectrum-pipeline

pip install -U .
```


# Execution

Below is an example to run the SPECTRUM pipeline :

```
python -W ignore ~/spectrum-pipeline/scripts/steles_pipeline.py --nightdir=20230605 -vp
```

The pipeline routines are organized in the following 5 main libraries:

* `pipeline_lib.py`: pipeline execution routines and functions
* `db.py`: an interface to create and manage a database of input/output data 
* `utils.py`: utility routines for reduction
* `products.py`: I/O routines containing the definition of SPECTRUM reduction products
* `product_plots.py`: routines to get diagnostic plots of reduction products

These libraries can also be used independently to reduce data step by step, as in the examples provided in the Jupyter [notebooks](https://github.com/edermartioli/spectrum-pipeline/tree/main/notebooks).

Download the [minidata package](https://drive.google.com/file/d/1tAVjyhYGMDcrU5sDdGCmd_f5HoazZ294/view?usp=drive_link) containing STELES/ECHARPE data to test the pipeline. You may also want to downaload the [minilcdata package](https://drive.google.com/file/d/1GJA7HB-j2YhbmLO82T1g-LNrbpYFn6OR/view?usp=drive_link) containing time series data. 

See the [ECHARPE Quick Tutorial](https://github.com/edermartioli/sparc4-pipeline/blob/257cde7c85666b2cd83a76834a9f0023365393fa/docs/Manual%20da%20SPARC4%20Pipeline.pdf) and [STELES Quick Tutorial](https://github.com/edermartioli/sparc4-pipeline/blob/257cde7c85666b2cd83a76834a9f0023365393fa/docs/Manual%20da%20SPARC4%20Pipeline.pdf)to start using the pipeline quickly.

The `spectrum-pipeline` is under development in collaboration with the scientific community. If you are interested in collaborating, send an email to the pipeline team at the following address: `spectrum-pipeline@googlegroups.com`.



