import gspread
import requests, sys
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

  
#This is where you place your key for the Google Sheet you'd like to update
gameKey = 'key'
    
#This function signs into the Google Sheet you are attempting to update, and grabs all information from the "Games" worksheet and returns it as an array to be passed to updateGamePricing
def readSheet():
  scope = ['https://spreadsheets.google.com/feeds']
  authorization = "yourGoogleJsonCredentials.json"
  credentials = ServiceAccountCredentials.from_json_keyfile_name(authorization, scope)
  gc = gspread.authorize(credentials)
  sh = gc.open_by_key(gameKey)
  worksheet = sh.worksheet("Games")
  ticketID_sheet = worksheet.get_all_values()
  return ticketID_sheet, worksheet


#This function takes the URL cell for each game, uses Requests to get the web page, and Beautifulsoup to parse the HTMl for the new price based on the condition column. The Google Sheet data has validation enabled for the Condition column, ensuring that the condition matches the 3 options on the site. It moves the Previous price from the Current Price cell to the Previous Price cell, and updates the Current Price cell with the data scraped from Pricecharting. It iterates through the entire sheet. This function accepts a command line argument that allows it to start at a certain row if the user would like.
def updateGamePricing(ticketID_sheet,worksheet):
#This Try-Except statement looks for a command line argument from a user to start at a certain row, and starts at the beginning if no argument is entered 
  try:
    if not len(sys.argv) < 1:
      if int(sys.argv[1]) < len(ticketID_sheet):
        count = int(sys.argv[1])
      else:
        count = 0
    else:
      count = 0 
  except:
    count = 0
  newone = ticketID_sheet[count:]
  dict = {'Used':0,'Complete':1,'New':2}
  for ticket in newone:
    if count >0:
      print (ticket[0]+ ' '+ ticket[1]+' Condition:'+ticket[3]+ ' New:'+ticket[6]+ ' Old:'+ticket[7])
      if ticket[9] == '' or ticket[9]=='N/A' or ticket[3] == '':
        print('Not enough info to scrape prices')
      else:
        condition = dict[ticket[3]]
        r = requests.get(ticket[9])
        soup = BeautifulSoup(r.text,"html.parser")
        td = [f.text.strip() for f in soup.find_all('span',{'class':'price'})]
        #Line 48 move the previous price to column G
        worksheet.update_acell('g'+str(count+1),ticket[5])
        #Line 50 looks up the new price for the condition 
        worksheet.update_acell('f'+str(count+1),td[condition])
      count = count+1
    else:
      count = count+1
      continue

def main():
  gamelist, worksheet = readSheet()
  updateGamePricing(gamelist,worksheet)
main()
