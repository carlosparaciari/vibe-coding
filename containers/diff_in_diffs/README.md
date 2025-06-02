# Difference-in-Differences (DiD) Tool

## Overview
This tool calculates the Difference-in-Differences (DiD) estimate from user-provided data in a CSV file. It uses an Ordinary Least Squares (OLS) regression to determine the impact of an intervention (treatment) by comparing a treatment group to a control group, both before and after the intervention.

## Input CSV Format
The input must be a CSV file with the following three columns:

*   `pre-period`: Indicates if the observation is from the pre-intervention period.
    *   **Data Type**: Boolean-like. Use `1` for true (pre-period) and `0` for false (post-period).
*   `treatment`: Indicates if the observation belongs to the treatment group.
    *   **Data Type**: Boolean-like. Use `1` for true (treatment group) and `0` for false (control group).
*   `target`: The outcome variable of interest.
    *   **Data Type**: Float (numeric).

**Example CSV Snippet:**
```csv
pre-period,treatment,target
1,0,10.5
1,1,12.0
0,0,15.2
0,1,20.8
1,0,11.3
1,1,13.1
0,0,16.0
0,1,22.5
```

## Output Format
The tool prints a JSON string to standard output containing the DiD coefficient and its corresponding p-value.

**Example Output:**
```json
{"did_coefficient": 3.0123, "p_value": 0.139}
```
*(Note: Actual values will depend on your input data.)*

## How to Build the Docker Image
Navigate to the `containers/diff_in_diffs` directory (where the `Dockerfile` is located) and run:
```bash
docker build -t did-tool .
```

## How to Run the Docker Container
To run the DiD analysis using the Docker image, you need to mount your input CSV file into the container and specify its path as a command-line argument.

The tool expects the path to the CSV file *inside the container*. A common practice is to mount your local data into a `/data` directory within the container.

**Example Command:**
Suppose your CSV file is located at `/home/user/my_data.csv` on your local machine.
```bash
docker run -v /home/user/my_data.csv:/data/input.csv did-tool /data/input.csv
```
In this command:
*   `-v /home/user/my_data.csv:/data/input.csv`: Mounts your local file `/home/user/my_data.csv` to `/data/input.csv` inside the container.
*   `did-tool`: The name of the Docker image you built.
*   `/data/input.csv`: The path to the input file *inside the container*, which is passed to the script.

The script will then process `/data/input.csv` and print the JSON results to your terminal.

## Running Tests
The application includes unit tests to verify the core DiD calculation logic. To run these tests:

1.  **Build the Docker image** as described above (if you haven't already).
2.  **Run the tests within a new container**:
    ```bash
    docker run did-tool python -m unittest discover tests
    ```
    This command executes the `unittest` module, which will discover and run tests located in the `/app/tests` directory inside the container.
    *(Note: The `WORKDIR` is `/app` in the Dockerfile, and tests are copied to `/app/tests`)*.

    Alternatively, if you want to run tests with a specific test file:
    ```bash
    docker run did-tool python -m unittest tests.test_modelling
    ```
