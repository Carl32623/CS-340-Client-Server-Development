# Grazioso Salvare Dashboard

## Overview
This repository contains **interactive data dashboard** developed for **Grazioso Salvare**, an orgainization specializing in training rescue animals.

The dashboard integrates with a **MongoDB databse** containing Austin Animal Center outcome data. It provides Grazioso Salvare staff with tools to efficiently filter, query, and visualize animal records, supporting their mission to identify and train suitable rescue animals.

Key features include:
 - Secure connection to a MongoDB database
 - Custom filters for breed, age, outcome type, and intake condition
 - Dynamic data table views
 - Interactive charts for outcome distribution
 - Geographic map visualization of animal intakes and outcomes

---

## Requirements
- **Pythone 3.9+**
- **Jupyter Notebook**

## Technologies Used
- **Python 3.9**
- **MongoDB** (database storage and retrieval)
- **PyMongo** (MongoDB Python Driver)
- **Dash and Plotly** (interactive visualizations and web framework)
- **Jupyter Notebook** (development)

---

## Installation & Setup
- **Clone the repository**
  ```bash
  git clone https://github.com/Carl32623/CS-340-Client-Server-Development.git
  cd CS-340-Client-Server-Development/Animal_Rescue_Dashboard_Project
  ```
  - Open Jupyter Notebook and upload the Animal_Rescue_Dashboard.ipynb and PyMongo_Driver.py files.
  - Open Animal_Rescue_Dashboard.ipynb file and run all cells.  Jupyter will start the app and output a URL.
  - Click the URL to open the dashboard.

---

## Functionality
The original state of the dashboard. The filter options users to easily sort through records by breed, age, initial condition, or outcome type.
![Datatable Screenshot](ScreenShots/Screenshot%201.png)

---

Users can view filtered animal records in dynamic tables.
![Graph & Map Screenshot](ScreenShots/Screenshot%204.png)

---

##Demo Video
<vidoe src="ScreenShots/C_LaLonde_ProjectTwo_Screencast.mp4" controls width="720"></video>
