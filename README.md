# MDSDR: Mutation-Drug Sensitivity Data Resource

**A Comprehensive Resource for Studying and Addressing Drug Resistance**

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)
6. [Acknowledgements](#acknowledgements)

## Introduction

Drug resistance poses a significant challenge in the treatment of various diseases. The Mutation-Drug Sensitivity Data Resource (MDSDR) is a comprehensive database that consolidates mutation-induced drug resistance data from diverse sources, providing a unified and user-friendly platform.

## Features

- Comprehensive data on mutation-induced drug resistance.
- Experimental data on protein-ligand affinity changes.
- Clinical insights on mutations leading to drug resistance.
- Gene-protein alignment and disease details.
- Detailed drug properties and annotations.
- User-friendly web interface for searching and analyzing data.

## Installation

### Prerequisites

- Python 3.7+
- MongoDB
- Flask
- Jupyter Notebook

### Steps

1. **Clone the repository**

   ```shell
   git clone https://github.com/your-username/mdsdr.git
   cd mdsdr
   ```
   
3. **Set up a virtual environment**

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
   
5. **Install the required packages**

   ```shell
   pip install -r requirements.txt
   ```
   
7. **Set up the MongoDB database**

   Make sure MongoDB is installed and running on your machine. You can follow the installation instructions [here](https://docs.mongodb.com/manual/installation/).

   Create a new database and import the provided data.

   ```shell
   mongoimport --db mdsdr --collection your_collection --file path/to/your/data.json
   ```
   
9. **Run the Flask web application**

   ```shell
   flask run
   ```
   
11. **Open your browser and navigate to**

   ```shell
   http://127.0.0.1:5000
   ```

## Usage

### Jupyter Notebooks

Several Jupyter Notebooks are provided for data preprocessing and analysis:

- **preprocess.ipynb**: Contains the preprocessing steps for the raw data.
- **database.ipynb**: Details the database setup and data integration.

To run these notebooks, navigate to the `notebooks` directory and start Jupyter Notebook:

```shell
jupyter notebook
```

Open the desired notebook and run the cells.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was supported by grants from STI 2030—Major Projects, the National Natural Science Foundation of China, the Natural Science Foundation of Shanghai, the Medical-Engineering Cross Foundation of Shanghai Jiao Tong University, SJTU Trans-med Awards Research, and the Shanghai Clinical Research Center for Mental Health.
