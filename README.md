# Data-Mining-CSE-572-project 
## Phase 2
- The final features set which we have considered have following features,
    - CGM velocity
    - Moving RMS velocity
    - Discrete Wavelet Transform
    - Fast Fourier Transform

- After comparing the validation set accuracies of individual models, we have finalized the following models
  
  - RandomForest
  - AdaBoost
  - XGBoost
  - Naive Bayes
  
  
- Individual Contributions
    - RandomForest -> Surya Vamsi Tenneti
    - AdaBoost -> Santhosh Kumar
    - XGBoost -> Sai Uttej Thunuguntla
    - Naive Bayes -> Aryan Prasad


## Steps to execute
- Run the Assignment2.py and after running, it asks for a test file name
```python
> python Assignment2.py
Please enter the test file name: 
```
- After running, 4 output files with the predictions from each model is generated with the following names,
    - RForest_output.csv
    - XGBoost_output.csv
    - Adaboost_output.csv
    - NaiveBayes_output.csv
  
## System specifications
- System should have **Python 3+ (64-bit)**
- The following libraries need to be installed
    - Numpy
    - Pandas
    - XGBoost
    - Scikit-learn
    - Pickle
    - pywt