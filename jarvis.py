# import webdriver used for signin 

import speech_recognition as sr
#from gtts import gTTS
import os
import openai
from config import apikey
import pyttsx3
import webbrowser
import datetime
import random




chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Sammit: {query}\n Jarvis: "
    response = openai.completions.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response.choices[0].text)

    chatStr += f"{response.choices[0].text}\n"

    return response.choices[0].text

    # with open(f"Openai/prompt- {random.randint(1, 231315645)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('using')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def ai(prompt):
    openai.api_key = apikey
    text = f"{prompt} \n ***************\n\n"

    response = openai.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)

    text += response.choices[0].text

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 231315645)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('using')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_song(song_name):
    base_url = "https://www.youtube.com/results?search_query="
    webbrowser.open(base_url + song_name)

def open_video(video_title):
    base_url = "https://www.youtube.com/results?search_query="
    webbrowser.open(base_url + video_title)

def open_channel(channel_name):
    base_url = "https://www.youtube.com/results?search_query="
    webbrowser.open(base_url + channel_name)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    
    
    say("Hello I am Jarvis AI made by Sammit Bathla sir...")
    while True:
        print("Listening...")
        query = takeCommand()
        
        # say("Sure sir...")
        sites = [["YouTube", "https://www.youtube.com"], ["Wikipedia", "https://www.wikipedia.com"], ["Google", "https://www.google.com"],
                 ["Pinterest", "https://www.pinterest.com"],
    ["Microsoft", "https://www.microsoft.com"],
    ["eBay", "https://www.ebay.com"],
    ["WhatsApp", "https://www.whatsapp.com"],
    ["Airbnb", "https://www.airbnb.com"],
    ["Spotify", "https://www.spotify.com"],
    ["Twitch", "https://www.twitch.tv"],
    ["PayPal", "https://www.paypal.com"],
    ["Tumblr", "https://www.tumblr.com"],
    ["BBC", "https://www.bbc.com"],
    ["Yahoo", "https://www.yahoo.com"],
    ["CNN", "https://www.cnn.com"],
    ["ESPN", "https://www.espn.com"],
    ["Quora", "https://www.quora.com"],
    ["GitHub", "https://www.github.com"],
    ["Adobe", "https://www.adobe.com"],
    ["IMDb", "https://www.imdb.com"],
    ["Stack Overflow", "https://stackoverflow.com"],
    ["Slack", "https://www.slack.com"],
    ["Dropbox", "https://www.dropbox.com"],
    ["Netflix", "https://www.netflix.com"],
    ["Reddit", "https://www.reddit.com"],
    ["Facebook", "https://www.facebook.com"],
    ["Twitter", "https://www.twitter.com"],
    ["Instagram", "https://www.instagram.com"],
    ["LinkedIn", "https://www.linkedin.com"],
    ["Google", "https://www.google.com"],
    ["YouTube", "https://www.youtube.com"],
    ["Wikipedia", "https://www.wikipedia.com"],
    ["Amazon", "https://www.amazon.com"],
    ["Gmail", "https://mail.google.com"],
    ["Apple", "https://www.apple.com"],
    ["Adobe", "https://www.adobe.com"],
    ["Bing", "https://www.bing.com"],
    ["CNN", "https://www.cnn.com"],
    ["Dropbox", "https://www.dropbox.com"],
    ["eBay", "https://www.ebay.com"],
    ["Etsy", "https://www.etsy.com"],
    ["FedEx", "https://www.fedex.com"],
    ["Forbes", "https://www.forbes.com"],
    ["GitHub", "https://www.github.com"],
    ["GoDaddy", "https://www.godaddy.com"],
    ["HBO", "https://www.hbo.com"],
    ["HP", "https://www.hp.com"],
    ["IBM", "https://www.ibm.com"],
    ["IKEA", "https://www.ikea.com"],
    ["In-N-Out Burger", "https://www.in-n-out.com"],
    ["Instagram", "https://www.instagram.com"],
    ["Intel", "https://www.intel.com"],
    ["JetBlue", "https://www.jetblue.com"],
    ["LEGO", "https://www.lego.com"],
    ["McDonald's", "https://www.mcdonalds.com"],
    ["Mercedes-Benz", "https://www.mercedes-benz.com"],
    ["Microsoft", "https://www.microsoft.com"],
    ["Nestle", "https://www.nestle.com"],
    ["Nike", "https://www.nike.com"],
    ["Nissan", "https://www.nissan.com"],
    ["Pepsi", "https://www.pepsi.com"],
    ["PlayStation", "https://www.playstation.com"],
    ["Reddit", "https://www.reddit.com"],
    ["Samsung", "https://www.samsung.com"],
    ["Skype", "https://www.skype.com"],
    ["Sony", "https://www.sony.com"],
    ["SpaceX", "https://www.spacex.com"],
    ["Starbucks", "https://www.starbucks.com"],
    ["T-Mobile", "https://www.t-mobile.com"],
    ["Target", "https://www.target.com"],
    ["Tesla", "https://www.tesla.com"],
    ["The New York Times", "https://www.nytimes.com"],
    ["Uber", "https://www.uber.com"],
    ["Vimeo", "https://www.vimeo.com"],
    ["Visa", "https://www.visa.com"],
    ["Walmart", "https://www.walmart.com"],
    ["WhatsApp", "https://www.whatsapp.com"],
    ["Xbox", "https://www.xbox.com"],
    ["Yahoo", "https://www.yahoo.com"],
    ["Zara", "https://www.zara.com"],
    ["Airbnb", "https://www.airbnb.com"],
    ["Audi", "https://www.audi.com"],
    ["BBC", "https://www.bbc.com"],
    ["Coca-Cola", "https://www.coca-cola.com"],
    ["Disney", "https://www.disney.com"],
    ["Ford", "https://www.ford.com"],
    ["Hulu", "https://www.hulu.com"],
    ["IBM", "https://www.ibm.com"],
    ["JPMorgan Chase", "https://www.jpmorganchase.com"],
    ["KFC", "https://www.kfc.com"],
    ["LinkedIn", "https://www.linkedin.com"],
    ["Macy's", "https://www.macys.com"],
    ["NASA", "https://www.nasa.gov"],
    ["Nike", "https://www.nike.com"],
    ["Nintendo", "https://www.nintendo.com"],
    ["Panasonic", "https://www.panasonic.com"],
    ["Pepsi", "https://www.pepsi.com"],
    ["Pizza Hut", "https://www.pizzahut.com"],
    ["Subway", "https://www.subway.com"],
    ["The Home Depot", "https://www.homedepot.com"],
    ["The Walt Disney Company", "https://www.thewaltdisneycompany.com"],
    ["Toyota", "https://www.toyota.com"],
    ["United Airlines", "https://www.united.com"],
    ["Verizon", "https://www.verizon.com"],
    ["YouTube", "https://www.youtube.com"],
                 ]
        for site in sites:
            
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

      #  if "Open music" in query:
       #     musicPath = "spotify"
        #say(query)
        
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            mins = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} baajjkkee {mins} minutes")
            
        if "thanks jarvis".lower() in query.lower() or "thank you".lower() in query.lower() or "thank you jarvis".lower() in query.lower():

            say("Aapki khiddmat mai sir...")
            
        if "Jarvis".lower() in query.lower() or "Hey Jarvis".lower() in query.lower() or "Jarvis Utho".lower() in query.lower():
            say("Yes Boss!")
            
        if "Badhiya kaam kia".lower() in query.lower() or "Shaabash".lower() in query.lower() or "Well Done".lower() in query.lower():
            say("Yeh tohh meraa faarrz thaa sir...")

        command = takeCommand()

        if "play song" in command.lower():
            song_name = command.lower().replace("play song", "").strip().replace(" ", "+")
            play_song(song_name)

        elif "open video" in command.lower():
            video_title = command.lower().replace("open video", "").strip().replace(" ", "+")
            open_video(video_title)

        elif "open channel" in command.lower():
            channel_name = command.lower().replace("open channel", "").strip().replace(" ", "+")
            open_channel(channel_name)

        # if "open VS Code".lower() in query.lower():
            # os.system(f"open )

        if "using gpt".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis quit".lower() in query.lower():
            exit()
        elif "Reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)





