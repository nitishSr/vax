import requests
from datetime import datetime

from config import config_data

BASE_URL = config_data["base_url"]
current_time = datetime.now()
todays_date = current_time.strftime("%d-%m-%Y")


def get_availability_by_pin(pincode, date=todays_date):
    """
    Gets the availability by pincode and date

    Accepts:
        pincode (str): Valid area pin code
        date (str, optional): The date to search slot in dd-mm-yyyy format,
                            defaults to today's date

    Returns:
        response (Response): response object
    """
    params = {"pincode": pincode, "date": date}
    response = requests.get(
        BASE_URL + "/v2/appointment/sessions/public/findByPin",
        params=params,
    )
    return response
