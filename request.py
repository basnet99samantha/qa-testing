import pandas as pd
import requests

# Specify the location of the URL list Excel file
url_location = 'Status.xlsx'


def check_url_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Pass", f"{url} is accessible (Status code: {response.status_code})"
        # elif response.status_code == 404:
        #     return "Fail", f"{url} returned a Not Found error (Status code: {response.status_code})"
        # elif response.status_code == 403:
        #     return "Fail", f"{url} returned a Forbidden error (Status code: {response.status_code})"
        elif response.status_code == 502:
            return "Fail", f"{url} returned an Internal Server Error (Status code: {response.status_code})"
        else:
            return "Fail", f"{url} returned an unexpected status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return "Fail", f"{url} could not be accessed ({e})"


def read_excel():
    # Read the URL list from the Excel file
    reader = pd.read_excel(url_location)
    results = []  # Initialize an empty list to store pass/fail outcomes
    statuses = []  # Initialize an empty list to store status messages

    for row, column in reader.iterrows():
        url = column["URL"]
        print(f"Checking {url}")

        # Check URL status
        result, status = check_url_status(url)
        results.append(result)
        statuses.append(status)

    # Add the results and statuses to the DataFrame
    reader["Result"] = results
    reader["Status"] = statuses

    # Save the updated DataFrame back to the same Excel file
    reader.to_excel(url_location, index=False)


if __name__ == '__main__':
    read_excel()
