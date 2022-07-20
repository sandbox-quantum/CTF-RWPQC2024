# Challenge 2. Attack on Trained Logistic Regression Model

The goal of this challenge is to perform an attack on a whitebox trained logistic regression model. The attacker has access to the following information:

- Trained logistic regression model weights (𝜃<sub>0</sub>,…,𝜃<sub>𝑘</sub>), trained on a dataset consisting of 𝑛 training examples, (𝐱<sub>𝑖</sub>,𝑦<sub>𝑖</sub>). You can assume the model converged, that 𝜃<sub>0</sub> is the intercept, and that ridge regularization (ℓ<sub>2</sub>-regularization with regularization parameter 1) was used.
- All but one (𝑛−1 total) of the training datapoints, {(𝐱<sub>1</sub>,𝑦<sub>1</sub>),…,(𝐱<sub>𝑛−1</sub>,𝑦<sub>𝑛−1</sub>)}

The attacker will have several .csv files to progress its attack and must consider certain restrictions on the training data.

## Training data constraints

Each feature set 𝐱<sub>𝑖</sub> consists of 𝑘=16 integers, each between −16 and 16 inclusive, and each label 𝑦𝑖 is binary 0 or 1.

## Challenge objective

The attacker's objective is to recover the missing training datapoint (𝐱<sub>𝑛</sub>,𝑦<sub>𝑛</sub>).
To evaluate your solution you need to send us the missing information to __ctf-rwpqc2024@sandboxaq.com__ with the subject "Challenge2".

## References

https://en.wikipedia.org/wiki/Logistic_regression
