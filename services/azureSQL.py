import pyodbc

server = 'infinities-xrii-server.database.windows.net'
database = 'infinities-xrii-db'
username = 'infinitiesxriiadmin'
password = '{!nf1nities}'
driver = '{ODBC Driver 17 for SQL Server}'


def get_connection_string():
    return pyodbc.connect('DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID='
                          + username + ';PWD=' + password)


def test_connection():
    conn = get_connection_string()
    with conn.cursor() as cursor:
        cursor.execute("SELECT @@Version")
        row = cursor.fetchall()
        return str(row)


def insert_account(idAccount, json):
    conn = get_connection_string()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (id, merchantID, url, organisationName, address, phone, email, verfiedEmail, "
                   "activeCardDetails, selectedPlan, monthlyTrackedUsers, averageDailyUsers, engagementRate, "
                   "retentionRate, stickyFactor, addOns) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   int(idAccount),
                   str(json.get("AccountData").get("MerchantID")),
                   str(json.get("AccountData").get("URL")),
                   str(json.get("AccountData").get("OrganisationName")),
                   str(json.get("AccountData").get("Address")),
                   str(json.get("AccountData").get("Phone")),
                   str(json.get("AccountData").get("Email")),
                   str(json.get("AccountData").get("VerfiedEmail")),
                   str(json.get("AccountData").get("ActiveCardDetails")),
                   str(json.get("AccountData").get("SelectedPlan")),
                   int(json.get("AccountData").get("MonthlyTrackedUsers")),
                   int(json.get("AccountData").get("AverageDailyUsers")),
                   float(json.get("AccountData").get("EngagementRate")),
                   float(json.get("AccountData").get("RetentionRate")),
                   float(json.get("AccountData").get("StickyFactor")),
                   str(json.get("AccountData").get("AddOns"))
                   )
    conn.commit()
    cursor.close()


def insert_contact(idContact, idAccount, json):
    conn = get_connection_string()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (id, email, merchantID, accountHolderName, mobile, verfiedEmail) "
                   "values(?,?,?,?,?,?)",
                   int(idContact),
                   str(json.get("ContactsData").get("Email")),
                   int(idAccount),
                   str(json.get("ContactsData").get("AccountHolderName")),
                   str(json.get("ContactsData").get("Mobile")),
                   int(json.get("ContactsData").get("VerfiedEmail") == True)
                   )
    conn.commit()
    cursor.close()
