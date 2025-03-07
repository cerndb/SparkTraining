## Training material for the course "Introduction to Spark APIs for Data Processing"

[![DOI](https://zenodo.org/badge/550234729.svg)](https://doi.org/10.5281/zenodo.14989474)
[![SWAN](https://swan.web.cern.ch/sites/swan.web.cern.ch/files/pictures/open_in_swan.svg)](https://cern.ch/swanserver/cgi-bin/go?projurl=https://github.com/cerndb/SparkTraining.git)
[<img src="https://colab.research.google.com/assets/colab-badge.svg">](https://colab.research.google.com/github/cerndb/SparkTraining)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cerndb/SparkTraining/master)
<a href="https://codespaces.new/cerndb/SparkTraining?devcontainer_path=.devcontainer%2FSparkTraining%2Fdevcontainer.json">
  <img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces" width="180">
</a>

### Course website with videos and slides: https://sparktraining.web.cern.ch/

## Contents

- [Notebooks with tutorials and exercises](notebooks)
- [Data used by the notebooks](data)
- [Code examples in Scala and Python](code)

See also the notebooks on display in the  [CERN SWAN Gallery](https://swan-gallery.web.cern.ch/apache_spark/)


Contact: Luca.Canali@cern.ch   

---
## Notebooks

### Session 1
[Tutorial-DataFrame.ipynb](notebooks/Tutorial-DataFrame.ipynb)  
[Solutions-DataFrame.ipynb](notebooks/Solutions-DataFrame.ipynb)  
[Examples-Pandas on Spark](notebooks/Examples_Pandas_on_Spark.ipynb)

### Session 2
[Tutorial-SparkSQL.ipynb](notebooks/Tutorial-SparkSQL.ipynb)  
[HandsOn-SparkSQL_exercises.ipynb](notebooks/HandsOn-SparkSQL_exercises.ipynb)  
[HandsOn-SparkSQL_with_solutions.ipynb](notebooks/HandsOn-SparkSQL_with_solutions.ipynb)    

### Session 3
[Tutorial-SparkStreaming.ipynb](notebooks/Tutorial-SparkStreaming.ipynb)  
[ML_Demo1_Classifier.ipynb](notebooks/ML_Demo1_Classifier.ipynb)  
[ML_Demo2_Regression.ipynb](notebooks/ML_Demo2_Regression.ipynb)  
[Spark_JDBC_Oracle.ipynb](notebooks/Spark_JDBC_Oracle.ipynb)  

### Session 4
[Demo_Spark_on_Hadoop.ipynb](notebooks/Demo_Spark_on_Hadoop.ipynb)  
[Demo_Dimuon_mass_spectrum.ipynb](notebooks/Demo_Dimuon_mass_spectrum.ipynb)    
[NXCals-example.ipynb](notebooks/NXCals-example.ipynb)  
[NXCals-example_bis.ipynb](notebooks/NXCals-example_bis.ipynb)  
[TPCDS_PySpark_CERN_SWAN_getstarted.ipynb](notebooks/TPCDS_PySpark_CERN_SWAN_getstarted.ipynb)  
  
### Additional SWAN gallery notebooks
[LHCb_OpenData_Spark.ipynb](notebooks/LHCb_OpenData_Spark.ipynb)  
[Dimuon_Spark_ROOT_RDataFrame.ipynb](notebooks/Dimuon_Spark_ROOT_RDataFrame.ipynb)  

---
## How to run the notebooks from CERN SWAN Notebook Service

- Open SWAN and clone the repo: [![SWAN](https://swan.web.cern.ch/sites/swan.web.cern.ch/files/pictures/open_in_swan.svg)](https://cern.ch/swanserver/cgi-bin/go?projurl=https://github.com/cerndb/SparkTraining.git)
   - note this can take a couple of minutes
   - as an alternative you can clone the repo from the SWAN GUI https://swan.web.cern.ch
     - find and click the button "Download project from git"
     - when prompted, clone the repo `https://github.com/cerndb/SparkTraining.git`
- Open the tutorial notebooks at SparkTraining -> notebooks

## How to run the notebooks from private Jupyter installations or other notebook services (Colab, Binder, etc)

- `pip install pyspark`
- `git clone https://github.com/cerndb/SparkTraining` 
   - or clone the image at `https://gitlab.cern.ch/db/SparkTraining`
- Start jupyter: `jupyter-notebook`
- Run the notebooks on GitHub Codespaces: <a href="https://codespaces.new/cerndb/SparkTraining?devcontainer_path=.devcontainer%2FSparkTraining%2Fdevcontainer.json">
  <img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces" width="180"></a>
- Run the notebooks on Colab: [<img src="https://colab.research.google.com/assets/colab-badge.svg">](https://colab.research.google.com/github/cerndb/SparkTraining)
  - With this option you will need also to download the data folder and `pip install pyspark`
- Run on binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cerndb/SparkTraining/master)

