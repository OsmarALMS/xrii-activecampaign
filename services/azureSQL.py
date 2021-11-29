import pyodbc
from datetime import datetime

server = 'infinities-xrii-server'
database = 'infinities-xrii-db'
username = 'infinitiesxriiadmin'
password = '!nf1nities'
driver = '{ODBC Driver 17 for SQL Server}'


def get_connection_string():
    return 'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' \
           + database + ';UID=' + username + ';PWD=' + password


def test_connection():
    conn = pyodbc.connect(get_connection_string())
    with conn.cursor() as cursor:
        cursor.execute("SELECT @@Version")
        row = cursor.fetchall()
        print(row)


def insert_json(json):
    now = datetime.now()
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO active_campaign (VerfiedEmail,OrganisationName,Email,Address,URL,Phone,MerchantID,"
                   "ActiveCardDetails,SelectedPlan,AddOns,MonthlyTrackedUsers,AverageDailyUsers,EngagementRate,"
                   "RetentionRate,StickyFactor,dtAddRow) values(?,?,?)",
                   json.get("VerfiedEmail"), json.get("OrganisationName"), json.get("Email"),
                   json.get("Address"), json.get("URL"), json.get("Phone"),
                   json.get("MerchantID"), json.get("ActiveCardDetails"), json.get("SelectedPlan"),
                   json.get("AddOns"), json.get("MonthlyTrackedUsers"), json.get("AverageDailyUsers"),
                   json.get("EngagementRate"), json.get("RetentionRate"), json.get("StickyFactor"),
                   datetime.timestamp(now))
    cnxn.commit()
    cursor.close()
