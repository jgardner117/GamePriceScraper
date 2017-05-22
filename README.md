# GamePriceScraper
This is a Python App I created to update the prices of my video game inventory Google Sheet in order to track the average value of my collection over time. This was a tedious process that was ripe for automation made possible by Python, BeautifulSoup and gSpread.

## Getting Started
First, you will want to set up a Good

### Prerequisites
This app requires the following prequisites:
  Python 3.4
  BeautifulSoup 4
  gSpread 0.6.2
  Google API key
  Google Drive/Sheets Account
  
## Installing

This app is pretty easy to install and run. First, you will want to set up a Google Sheet formatted as follows:

| System | Game Title | Missing | Condition | Comments | Avg Current Price (pricecharting.com) | Avg Past Price (pricecharting.com) | TCRF.net Links | Interesting Links | Pricecharting.com link |
|--------|------------|---------|-----------|----------|---------------------------------------|------------------------------------|----------------|-------------------|------------------------|

The code parses the URL from cell J, and looks for the CSS SPAN class "Price" for the game and compares it to the value in cell D. In order for this to work I implemented data validation in Google Sheets for column d to have to be one of the 3 following condition values that correspond 1:1 with the conditions found on PriceCharting.net:

Used

Complete

New

The code can be easily changed to fit any layout by simply changing the indexes of the array within the updateGamePricing function. After setting up the Sheet, you'll want to get an API key by following the directions here:https://developers.google.com/sheets/api/guides/authorizing

Once you have created a Developer Account and created an API key, you'll want to place the .json file in the same folder as GamePriceScraper.py, and update the line of code that says "authorization = "yourGoogleJsonCredentials.json" with the name of the JSON file. After that, navigate to the Google Sheet that you created and click the "Share" button, and invite the email address in the JSON file labelled "Client_ID" to edit the document. 

Finally, look at the url of the Google Sheet. The URL contains the key, or the exact path, to the document you'd like to edit. Copy the key from the url into line 8 of the GamePriceScraper. 

With the url:
https://docs.google.com/spreadsheets/d/1234testyoururlhere-0/edit#gid=0

Your code should look like:

 #This is where you place your key for the Google Sheet you'd like to update
 
gameKey = '1234testyoururlhere' 

For added information at a glance I have also set up conditional formatting on cells F and G to turn cells red or green based on whether the game is increasing or decreasing in average value over time.

## Running
There are two options the user is given when starting this app. If you pass a numerical command line argument to the Python Script, it will attempt to start updating prices at that line in the Google Sheet. If there is no numerical command line argument given, the app will begin on line 1 to account for headers.

The app will iterate through every game in the Sheet, and move the value from cell F to cell G, and update cell F to the new price. If a game does not have a URL, the URL could not be reached, or the game has an inappropriate condition, the scraper will move on to the next item in the sheet.

## Authors

* **Jesse Gardner** - *Developer* - [HatePH34R](https://github.com/HatePH34R)

See also the list of [contributors](https://github.com/hateph34r/GamePriceScraper/contributors) who participated in this project.


