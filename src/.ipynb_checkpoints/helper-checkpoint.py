
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def bootstrap_sample_medians(data, n_bootstrap_samples=10**4):
    '''
    Parameter: an array of samples.
    n_bootstrap_samples(default 10**4): the number of simulations.
    
    Return a list of medians values from bootstrapping.
    '''
    bootstrap_sample_medians = []
    for i in range(n_bootstrap_samples):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_sample_medians.append(np.median(bootstrap_sample))
    return bootstrap_sample_medians


def bootstrap_sample_mean(data, n_bootstrap_samples=10**4):
    '''
    Parameter: an array of samples.
    n_bootstrap_samples(default 10**4): the number of simulations.
    
    Return a list of mean values from bootstrapping.
    '''
    bootstrap_sample_mean = []
    for i in range(n_bootstrap_samples):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_sample_mean.append(np.mean(bootstrap_sample))
    return bootstrap_sample_mean


def corr_heatmap(data):
    '''
    Parameter: DataFrame
    Returns a correlations heatmap with annotaions. 
    '''
    plt.figure(figsize = (16,5))
    ax = sns.heatmap(data.corr(), annot = True)

    
