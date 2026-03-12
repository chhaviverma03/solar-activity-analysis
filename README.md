# solar-activity-analysis
# Solar Activity Data Visualization

This project analyzes historical solar activity using sunspot datasets to study patterns in solar behavior over time.

## Overview
Solar activity follows periodic cycles that influence space weather and satellite communication systems. In this project, historical sunspot data is analyzed and visualized to observe these periodic patterns.

## Features
- Time-series visualization of solar activity using sunspot data
- Identification of periodic solar cycles (~11 years)
- Frequency analysis of solar activity using Fast Fourier Transform (FFT)

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib

## Files
- `solar_activity_analysis.py` – Python script for data analysis and visualization
- `SN_m_tot_V2.0.csv` – Sunspot dataset
- `solar_activity_plot.png` – Solar activity time-series plot
- `solar_fft_spectrum.png` – Frequency spectrum of solar activity

## Dataset
The dataset used is the **International Sunspot Number dataset** provided by the Solar Influences Data Analysis Center (SIDC).

Source:
https://www.sidc.be/silso/datafiles

## Output
The project generates:
- A time-series plot showing solar activity from 1749 to the present
- A frequency spectrum revealing the dominant solar cycle

## Purpose
This project demonstrates basic **time-series analysis and signal processing techniques** applied to real solar data.
