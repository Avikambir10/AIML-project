# AIML-project
# Wine Quality Analysis

This project performs a comprehensive analysis of a wine dataset, using Python and popular data analysis libraries. The dataset contains chemical properties of different wines, which are used to predict their quality.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Techniques Used](#techniques-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Libraries Used](#libraries-used)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to understand the relationships between various attributes of wine (such as acidity, sugar content, and alcohol levels) and the overall quality. By analyzing these factors, we aim to discover which chemical properties contribute most to a wine's quality.

## Features

- Load and visualize the wine dataset.
- Exploratory Data Analysis (EDA) to understand the relationships between features.
- Correlation analysis to identify key contributors to wine quality.
- Perform various classification techniques to predict wine quality.
- Use of data visualization techniques (e.g., seaborn, matplotlib) to present insights.

## Techniques Used

1. **Exploratory Data Analysis (EDA)**: 
   - EDA was conducted to summarize the dataset's main characteristics. It included visual methods to uncover relationships between variables, detect anomalies, and outliers.

2. **Logistic Regression**:
   - Logistic Regression was applied as a classification technique to predict wine quality based on its features. 
   - The model was trained using `LogisticRegressionCV`, which performs cross-validation to optimize the model's parameters.

3. **Decision Tree**:
   - A Decision Tree Classifier was implemented to model the decision-making process by learning simple decision rules inferred from the dataset features.

4. **Random Forest**:
   - Random Forest, an ensemble learning technique, was used to improve the prediction accuracy by creating multiple decision trees and merging them to get a more accurate and stable prediction.

5. **Support Vector Machine (SVM)**:
   - The Support Vector Machine (SVM) model was used to classify the wine data by finding the hyperplane that best separates the different classes.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/wine-quality-analysis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd wine-quality-analysis
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once you have cloned the repository and installed the dependencies, open the Jupyter Notebook and execute the cells to perform the analysis:

1. Launch Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

2. Open the `wine.ipynb` file and run the notebook cells to load the dataset, perform analysis, and visualize the results.

## Dataset

The dataset used for this analysis contains the following features:

- **Fixed acidity**
- **Volatile acidity**
- **Citric acid**
- **Residual sugar**
- **Chlorides**
- **Free sulfur dioxide**
- **Total sulfur dioxide**
- **Density**
- **pH**
- **Sulphates**
- **Alcohol**
- **Quality** (target variable)

## Libraries Used

- **Python 3.x**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.
