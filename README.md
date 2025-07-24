# Modified Gale-Shapley Algorithm for Hospital-Student Matching

## Overview
This project implements a modified version of the Gale-Shapley algorithm to handle hospital-student matching with unequal numbers of participants and multiple capacity constraints.

## Problem Statement
Traditional Gale-Shapley algorithm assumes equal numbers of participants in both groups, with one-to-one matching. However, real-world hospital-student matching often involves:
- More graduating students than available hospital positions
- Hospitals with multiple residency slots
- Need to fill all available hospital positions optimally

## Features
- Handles unequal numbers of students and hospitals
- Supports multiple capacity per hospital
- Maintains stable matching properties

## Implementation Details

### Input Format
- CSV file or Text file with two sections (refer input_data for samples):
1. Hospital data
  - Hospital name, slots and hospital's preferences of residents
2. Resident data
  - Resident name, resident's preferences of hospitals

The input should be in the order of Hospital name, slots (vacancy) and Hospital preference List with a blank line in between and then the Resident list in the order of Resident name and Resident’s Preference List.

## Running the code
- Add .csv/.txt file in input_data folder
- input_data folder also has some test data which we tested with
- Change the file path in path variable under main()
- Run the gale_shapley_algo.py
- Output will be saved under output_data folder as 'match_result_{timestamp}.txt'
