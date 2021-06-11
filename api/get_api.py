import requests
from datetime import datetime, timedelta

from config import config_data

BASE_URL = config_data["base_url"]
current_time = datetime.now()
todays_date = current_time.strftime("%d-%m-%Y")
tomorrow = current_time + timedelta(days=1)
tomorrows_date = tomorrow.strftime("%d-%m-%Y")
dates_to_search = [todays_date, tomorrows_date]


def get_availability_by_pin(pincode, date):
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


def get_vaccine_slots(pincode):
    """
    Gets the availability by pincode for today's and tomorrow's date

    Accepts:
        pincode (str): Valid area pin code

    Returns:
        vaccine_date (list): List containing json data fetched from get api
        msg_str (str): The message string containing errors if any
    """
    vaccine_data = []
    msg_str = ""
    try:
        for date_search in dates_to_search:
            res = get_availability_by_pin(pincode, date_search)
            if res.status_code == 200:
                fetched_data = res.json()
                vaccine_data.append(fetched_data["sessions"])
            else:
                msg_str = "Slot availability data could not fetched, please try again in some time !\
                    \n Server returned : {}".format(res.text)
                break
    except Exception as err:
        msg_str = err
    return vaccine_data, msg_str
