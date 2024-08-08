import numpy as np

# Original data
data = np.array([475, 344, 443, 427, 563, 500, 457, 372, 584, 406, 405, 453])

# Number of bootstrap samples
n_bootstrap = 2000

# Function to generate bootstrap samples and calculate sample means
def bootstrap_means(data, n_bootstrap):
    np.random.seed(0)  # for reproducibility
    bootstrap_samples = np.random.choice(data, (n_bootstrap, len(data)), replace=True)
    sample_means = np.mean(bootstrap_samples, axis=1)
    return sample_means

# Generate bootstrap sample means
bootstrap_sample_means = bootstrap_means(data, n_bootstrap)

# Sample mean of the first bootstrap sample
sample_mean_first_bootstrap = bootstrap_sample_means[0]

# 95% confidence interval
lower_bound = np.percentile(bootstrap_sample_means, 2.5)
upper_bound = np.percentile(bootstrap_sample_means, 97.5)
confidence_interval = (lower_bound, upper_bound)

print(sample_mean_first_bootstrap, confidence_interval)