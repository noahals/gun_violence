from bs4 import BeautifulSoup
import mysql.connector
import time
from datetime import datetime
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains


def Collection(page):
    # Using Beautiful soup to make contents iterable
    soup = BeautifulSoup(page, 'html.parser')
    val = []

    # Finding all instances of the class containing the players names
    incidents = soup.find_all("tr", class_="odd")

    # Iterating through data tables and placing them in tuples to be sent to SQL database
    for a in incidents:
        temp_row = []
        for x in a:
            temp_row.append(x.text.strip())
        temp_row.pop(7)
        temp_row.pop(7)
        temp_row.pop(4)
        date = time.strptime(temp_row[1], "%B %d, %Y")
        temp_row[1] = datetime.fromtimestamp(time.mktime(date))
        val.append(tuple(temp_row))

    return val





if __name__ == "__main__":
    #Connecting to mysql database
    mydb = mysql.connector.connect(
        host="localhost",
        user="noahalsina",
        database="mass_shootings"
    )

    mycursor = mydb.cursor()

    #stating the sql query
    sql = "INSERT IGNORE INTO incidents (id, date, state, city, deaths, injured) VALUES (%s, %s, %s, %s, %s, %s)"
    val = []

    print("----------------EXTRACTING DATA----------------")
    # url containing information being loaded into driver
    URL = 'https://www.gunviolencearchive.org/last-72-hours'

    #setting the chrome options to not open a window
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument('--headless')
    driver = uc.Chrome(options=options)

    #opening the chrome window
    driver.get(URL)
    time.sleep(8)


    try:
        actions = ActionChains(driver)
        # Looping through all the pages until it reaches the last page
        while True:
            #Using the XPATH of the next button to determine the location on the page
            next = driver.find_element(By.XPATH, '//a[@title="Go to next page"]')

            # Appending data to the value list by calling the Collection function
            for x in Collection(driver.page_source):
                val.append(x)

            # Moving the screen down to the next button
            actions.move_to_element(next).perform()
            time.sleep(1)

            # Clicking the next button
            next.click()
    except:
        pass
    finally:
        driver.quit

        # Executing the data to the SQL server
        mycursor.executemany(sql, val)
        mydb.commit()
        print("done!")


