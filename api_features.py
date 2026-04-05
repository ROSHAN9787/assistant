import wikipedia
from datetime import datetime
import webbrowser

wikipedia.set_lang("en")

def get_wikipedia_info(query):
    query = query.lower()
    remove = ["who is", "what is", "tell me", "about"]
    for r in remove:
        query = query.replace(r, "")
    query = query.strip()

    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Please be specific. Try {e.options[0]}"
    except:
        return "Sorry, I could not find information on that."

def get_time():
    return datetime.now().strftime("The time is %I:%M %p")

def get_day_date():
    return datetime.now().strftime("Today is %A, %d %B %Y")

def open_google():
    webbrowser.open("https://www.google.com")
    return "Opening Google"
def open_youtube():
    webbrowser.open("https://www.youtube.com/")
    return "Opening youtube"
