from datetime import datetime, date
CURRENT_MILES = 865.2
def thisWorks(a,b):
    print("Hello" + a + "you have run " + str(b) + " miles this year")
    dayOfYear = datetime.now().timetuple().tm_yday
    avg = b / dayOfYear
    print(avg)
    print("That's an average of " + avg + "miles per day")
    return avg

if __name__ == "__main__":
    try:
        name = "Jonathan"
        avg = thisWorks(name,CURRENT_MILES)
        activities = ["running", "walking", "biking"]
        print("List of activities:")
        i = 0
        while i < len(activities):
            print(activities[i])
            i += 1
    except:
        pass
    