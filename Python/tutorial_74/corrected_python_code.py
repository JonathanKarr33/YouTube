from datetime import datetime
def avg_miles_run_per_day(name : str, miles : float)-> float:
    """
    This function calculates the number of miles someone
    has run per day this year
    Parameters:
    name (str): the person's name
    miles (float) : the number of miles someone has run this year
    Returns:
    avg_miles_run (float): the average miles someone has run this year
    """
    print(f"Hello {name} you have run {miles} miles this year")
    day_of_year = datetime.now().timetuple().tm_yday
    avg_miles_run = round(miles / day_of_year,2)
    print(f"That's an average of {avg_miles_run} miles per day")
    return avg_miles_run

if __name__ == "__main__":
    name = "Jonathan"
    current_miles = 865.2
    avg_miles_run_per_day(name,current_miles)
    activities = ["running", "walking", "biking"]
    print("List of activities:")
    for activtity in activities:
        print(activtity)

        x = "Jonathan"

        name = "Jonathan"