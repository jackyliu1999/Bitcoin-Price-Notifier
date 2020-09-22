from selenium import webdriver
import pyttsx3 as p #pip install pyttsx3

BitcoinURL = "https://finance.yahoo.com/quote/BTC-CAD/"

textToSpeech = p.init()
voices = textToSpeech.getProperty("voices") #array of default text to speech voices
textToSpeech.setProperty("voice", voices[1].id) #voice of id 1
textToSpeech.setProperty('rate',120) #slows down voice

benchmark = float(input("What benchmark would you like to set?\n"))
higher = input("Input True to be notified when price is higher than benchmark and False to be notified when lower:  \n")
displayHigher = False
if higher.lower() == "true" or higher.lower()=="t" or higher.lower()=="yes" or higher.lower()=="y":
    displayHigher = True
display = input("Would you like prices to be displayed?\n")
displayPrice = False
if display.lower() == "true" or display.lower()=="t" or display.lower()=="yes" or display.lower()=="y":
    displayPrice = True

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver', options=options)
while True:
    driver.get(BitcoinURL)
    sale = driver.find_element_by_class_name('YDC-Lead-Stack')
    x = driver.find_element_by_id('YDC-Lead-Stack-Composite').find_element_by_id("mrt-node-Lead-3-QuoteHeader")
    x = x.find_element_by_id("Lead-3-QuoteHeader-Proxy").find_element_by_id("quote-header-info")
    x = x.text.split("\n")
    typeOf = ""
    if "+" in x[3]:
        x = x[3].split("+")
        typeOf = "Increasing"
    elif "-" in x[3]:
        x = x[3].split("-")
        typeOf = "Decreasing"
    currentPrice = float(x[0].replace(",",""))
    if displayPrice == True:
        print(currentPrice)
    if currentPrice > benchmark:
        if displayHigher == True:
            print(str(currentPrice) + " is higher than benchmark: " + str(benchmark))
            driver.quit()
            textToSpeech.say("Price is higher than benchmark")
            textToSpeech.runAndWait()
            break
    if currentPrice < benchmark:
        if displayHigher == False:
            print(str(currentPrice) + " is lower than benchmark: " + str(benchmark))
            driver.quit()
            textToSpeech.say("Price is lower than benchmark")
            textToSpeech.runAndWait()
            break
