**README**

# CSC 1302 Project: Analysis and Visualization of Cooler Fan Vibration Data

This Python script is developed for the CSC 1302 project, focusing on the analysis, visualization, and machine learning aspects of accelerometer data collected from vibrations of a cooler fan with weights on its blades. The dataset can be used for various tasks, including prediction, classification, and vibration analysis, particularly in engines.

**Dataset Information**

- The dataset contains accelerometer data collected from a cooler fan with weights attached to its blades.
- It consists of 5 attributes: `wconfid`, `pctid`, `x`, `y`, and `z`.
- `wconfid`: Weight Configuration ID (1 - 'red', 2 - 'blue', 3 - 'green').
- `pctid`: Cooler Fan RPM Speed Percentage ID.
- `x`, `y`, `z`: Accelerometer values in three directions.
- The data was collected at different rotation speeds ranging from 20% to 100% of the cooler's maximum speed.

**Script Functionality**

1. **Data Manipulation**
   - Allows users to insert or delete rows from the dataset.

2. **Data Analysis**
   - Provides options to view top or bottom records, display statistics of the dataframe, and obtain information about the dataframe.

3. **Data Visualization**
   - Offers various visualization options, including histograms of numeric columns, line charts, scatter plots, and pair plots.

4. **Machine Learning**
   - Performs data preprocessing and splits the dataset into training and testing sets.
   - Implements Linear Regression and Random Forest Regression models to predict acceleration based on weight configuration and cooler fan RPM speed percentage.
   - Evaluates model performance using mean absolute error.

**Usage Instructions**

1. **Data Input**
   - Users are prompted to input the filename of the dataset (either CSV or XLSX format).

2. **Main Menu**
   - After loading the dataset, users can choose from four main options: Manipulation, Analysis, Visualization, Machine Learning, or Exit.

3. **Manipulation**
   - Option to insert or delete rows from the dataset.

4. **Analysis**
   - Provides options to view records, statistics, and information about the dataframe.

5. **Visualization**
   - Offers various visualization options to explore the data visually.

6. **Machine Learning**
   - Performs data preprocessing, model training, and evaluation.

**Dependencies**

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

**Additional Notes**

- The script adds a new column 'acceleration' to the dataset, representing the resultant acceleration calculated from the accelerometer values in the x, y, and z directions.
- Users can explore and analyze the data interactively using the provided functionalities.

**Disclaimer**

- This script is developed as part of a project assignment for educational purposes and may require further customization for specific use cases or datasets.

Feel free to reach out if you have any questions or suggestions for improvements.
