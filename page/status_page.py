# page/status_page.py

from page.base_page import get_status_code


def check_status(url):
    # Get the status code for the given URL
    status_code = get_status_code(url)

    # Determine the status based on the status code
    if status_code is None:
        return "Error", "Fail"
    elif status_code == 200:
        return status_code, "Pass"
    else:
        return status_code, "Fail"


class StatusPage:
    pass
