import pyodbc

server = 'infinities-xrii-server.database.windows.net'
database = 'infinities-xrii-db'
username = 'infinitiesxriiadmin'
password = '{!nf1nities}'
driver = '{ODBC Driver 17 for SQL Server}'


def get_connection_string():
    return pyodbc.connect('DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' \
           + username + ';PWD=' + password)


def test_connection():
    conn = get_connection_string()
    with conn.cursor() as cursor:
        cursor.execute("SELECT @@Version")
        row = cursor.fetchall()
        return str(row)


def insert_json(json):
    conn = get_connection_string()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO active_campaign (VerfiedEmail,OrganisationName,Email,Address,URL,Phone,MerchantID,"
                   "ActiveCardDetails,SelectedPlan,AddOns,MonthlyTrackedUsers,AverageDailyUsers,EngagementRate,"
                   "RetentionRate,StickyFactor) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   str(json.get("AccountData").get("VerfiedEmail")),
                   str(json.get("AccountData").get("OrganisationName")),
                   str(json.get("AccountData").get("Email")),
                   str(json.get("AccountData").get("Address")),
                   str(json.get("AccountData").get("URL")),
                   str(json.get("AccountData").get("Phone")),
                   str(json.get("AccountData").get("MerchantID")),
                   str(json.get("AccountData").get("ActiveCardDetails")),
                   str(json.get("AccountData").get("SelectedPlan")),
                   str(json.get("AccountData").get("AddOns")),
                   int(json.get("AccountData").get("MonthlyTrackedUsers")),
                   int(json.get("AccountData").get("AverageDailyUsers")),
                   float(json.get("AccountData").get("EngagementRate")),
                   float(json.get("AccountData").get("RetentionRate")),
                   float(json.get("AccountData").get("StickyFactor"))
                   )
    conn.commit()
    cursor.close()
