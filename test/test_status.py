from page.status_page import StatusPage, check_status
from utilities.file_utils import read_urls, write_results
from configuration.config import CSV_INPUT_FILE, CSV_OUTPUT_FILE


def test_check_website_status():
    # Instantiate the StatusPage object
    StatusPage()

    # Read URLs from CSV
    df = read_urls(CSV_INPUT_FILE)

    # Check status for each URL and update DataFrame
    for index, row in df.iterrows():
        url = row['url']
        status_code, status = check_status(url)
        df.at[index, 'status_code'] = status_code
        df.at[index, 'status'] = status

    # Write results back to CSV
    write_results(CSV_OUTPUT_FILE, df)

    print(f"Status check complete. Results saved to '{CSV_OUTPUT_FILE}'.")


# Run the test case
if __name__ == "__main__":
    test_check_website_status()
