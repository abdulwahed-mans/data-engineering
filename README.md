# Data-Engineering

ETL (Extract, Transform, Load) pipeline for banking demo data

# Bank Marketing Data Analysis

This project aims to analyze bank marketing data using Python's pandas and numpy libraries. The dataset consists of information about clients obtained from various marketing campaigns.

## Modules Used

- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical computing.
- `os`: For interacting with the operating system.

## Dataset

The dataset used in this project is stored in a CSV file named `clients.csv` located in the `input` directory.

### Columns (Headers) in the Clients CSV File

- `age`: Age of the client.
- `job`: Type of job.
- `marital`: Marital status.
- `education`: Level of education.
- `default`: Whether the client has credit in default (yes/no).
- `balance`: Average yearly balance, in euros.
- `housing`: Whether the client has a housing loan (yes/no).
- `loan`: Whether the client has a personal loan (yes/no).
- `contact`: Type of communication contact.
- `day`: Last contact day of the month.
- `month`: Last contact month of the year.
- `duration`: Last contact duration, in seconds.
- `campaign`: Number of contacts performed during this campaign and for this client.
- `pdays`: Number of days since the client was last contacted from a previous campaign.
- `previous`: Number of contacts performed before this campaign and for this client.
- `poutcome`: Outcome of the previous marketing campaign.
- `y`: Whether the client has subscribed to a term deposit (yes/no).

## Usage

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project_directory>
   ```

3. Run the analysis script:

   ```bash
   python analyze_data.py
   ```

## Contribution

Contributions are welcome! If you'd like to contribute to this project, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
