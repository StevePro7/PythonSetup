Launch PyCharm  
New project  
Base conda  

conda activate base  
python --version  
Python 3.9.12  


conda create -n MLtest python=3.10.19  
conda activate MLtest  

conda install -c conda-forge tensorflow  
TF NOT compatible w/ 3.9  

retry  
conda deactivate  
conda env list  

conda remove --name Mltest --all  

conda create -n tf python=3.10  
conda activate tf  
conda install -c conda-forge tensorflow  

which python  
~/anaconda3/envs/tf/bin/python   
~/anaconda3/envs/tf/bin/python --version  
3.10.19  

Other packages  
conda install -c conda-forge matplotlib  
conda install -c conda-forge scikit-learn  
conda install -c conda-forge pandas  
conda install -c conda-forge scipy  

conda env export --name tf > environment.yaml  
conda env create -f environment.yaml  

INSTALL
conda deactivate  
conda env create -f environment.yaml    