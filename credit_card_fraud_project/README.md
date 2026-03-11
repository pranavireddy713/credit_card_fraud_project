# Credit Card Fraud Detection System 💳🛡️

## Project Overview
The **Credit Card Fraud Detection System** is a full-stack web application designed to simulate real-world financial security protocols. It evaluates user-inputted transaction details and applies intelligent pattern-matching logic to flag potentially fraudulent activities, outputting a precise Fraud Risk Score (%).

## Problem Statement
Financial institutions lose billions annually to credit card fraud. Detecting anomalous transactions in real-time is critical. High transaction amounts at unusual hours, unrecognized IP locations, and rapid successive purchases are strong indicators of potential account compromise. This project provides an automated tool to evaluate these risk factors dynamically.

## Technologies Used
* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Jinja2 (Templating)
* **Architecture:** MVC (Model-View-Controller) structure adapted for Flask

## Key Features
* **Intelligent Rule-Based Analysis:** Analyzes transaction amount, time, location, merchant type, and 24-hour frequency.
* **Risk Scoring System:** Generates a 0-100% risk score based on aggregated threat factors.
* **Dynamic Visual Feedback:** Clean UI that immediately alerts users with color-coded indicators (Green = Safe, Red = Potential Fraud).
* **Responsive Design:** Fully functional and aesthetically pleasing on both desktop and mobile devices.

## System Workflow
1. User inputs transaction details via the web form.
2. Form data is submitted via a `POST` request to the Flask backend.
3. The Python algorithm processes the parameters against pre-defined threat vectors.
4. A cumulative risk score is calculated and bounded.
5. The system determines the safety status (Threshold: ≥50% is flagged as Fraud).
6. Results are rendered dynamically on the frontend.

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection