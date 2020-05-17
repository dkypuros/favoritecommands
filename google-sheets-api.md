

```

pip install --upgrade google-cloud --user

python -m pip install gspread --user

# To login to google account.
python -m pip install google-api-python-client


# Interactive Python Shell
# our application or a script is accessing spreadsheets on behalf of an end user

python
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#New Way to interact with google sheets via api.
https://gspread.readthedocs.io/en/latest/oauth2.html

> Head to Google Developers Console and create a new project (or select the one you already have).

Under “APIs & Services > Library”, search for “Drive API” and enable it.
Under “APIs & Services > Library”, search for “Sheets API” and enable it.

https://console.developers.google.com/apis/dashboard?folder=&organizationId=&project=my-project-79507

Look for + sign, and look for drive and sheets api. (click enable.)

My Project 79507
Project ID: my-project-79507
actions > permissions.

#oauth consent screen
app79507

```


```
import gspread

gc = gspread.oauth()

sh = gc.open("Example spreadsheet")

print(sh.sheet1.get('A1'))

```
