# Superstore Sales Dashboard
![image](https://github.com/KaranKathur06/Python-Dashboard/assets/155360397/256479c6-b416-4735-90da-3c2b22a07191)

![image](https://github.com/KaranKathur06/Python-Dashboard/assets/155360397/317f873c-dc57-4b82-916c-fe42586065a9)



## Overview

The **Superstore Sales Dashboard** is an interactive web application built with Python and Streamlit. It provides comprehensive insights into the sales data of a superstore, allowing users to filter and visualize sales performance across different regions, states, cities, and product categories.

### Key Features:
- **Date Range Filtering:** View sales data within a specific date range.
- **Dynamic Filtering:** Filter data based on region, state, and city.
- **Sales Analysis:** Visualize sales by category, region, segment, and time series.
- **Hierarchical Views:** Explore sales data using treemaps for a hierarchical breakdown.
- **Detailed Views:** Access detailed data summaries and download filtered datasets.

## Setup Instructions

Follow these steps to set up and run the Superstore Sales Dashboard locally on your machine.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- [Anaconda](https://www.anaconda.com/products/distribution) (optional, but recommended for managing dependencies)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/KaranKathur06/superstore-sales-dashboard.git
   cd superstore-sales-dashboard
   ```
   
2.**Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3.***Activate the Virtual Environment:***
  Windows:
  ```bash
   venv\Scripts\activate
 ```
 MacOS/Linux:
 ```bash
  source venv/bin/activate
 ```

4.Install Dependencies:
 ``` bash
    pip install -r requirements.txt
 ```
 If requirements.txt is not provided, install the necessary libraries manually:
 ```bash
 pip install streamlit pandas plotly
```

5.Navigate to the Project Directory(As per you saved):
 ```bash
cd C:\\STUDY\\PROGRAMS\\PYTHON\\DMDW_Project (AS PER MINE EXAMPLE)
```

6.Now run the Streamlit App:
```bash
 streamlit run dashboard.py
```

### Usage
-> **Date Range Filtering:** Use the date pickers to filter data within the selected start and end dates.
-> **Region Filtering:** Select one or more regions from the sidebar to filter the data accordingly.
-> **Optional State and City Filters:** Further refine your selection by choosing specific states and cities.
-> **View and Download Data:** Use the expanders and download buttons to view and save the filtered data.
-> **Visualize Sales:** Explore various charts and visualizations for in-depth sales analysis.


### Project Structure
-> `dashboard.py:` The main script that runs the Streamlit dashboard.
-> `SuperStoreDataSet.csv:` The dataset containing the superstore sales data.
-> `requirements.txt:` A list of Python packages required to run the project.


## Screenshots:
  Dashboard Overview
  Sales by Category


## Contributing:
 **Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.**

1.Fork the repository.

2.Create a new branch:
```bash
 git checkout -b feature-branch-name
```

3.Commit your changes:
```bash
 git commit -m 'Add some feature'
```

4.Push to the branch:
```bash
 git push origin feature-branch-name
```
5.Open a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
