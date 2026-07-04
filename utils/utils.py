from agent.runtime import ask_llm
from tools.tasks import add_task, remove_task, list_tasks
from tools.web import web_search
from voice.speak import speak
from voice.listener import listen_once
from tools.record import record, open_recordings_folder


def ask_user():

    prompt = listen_once().lower().strip()

    if "terminate" in prompt.lower() or "terminated" in prompt.lower():
        return "terminate"

    if "go to sleep" in prompt.lower() or "sleep" in prompt.lower():
        return "go to sleep"

    output = ask_llm(prompt)

    print(output)

    if prompt is None or prompt == "":
        return

    if "intent" not in output:
        speak("I couldn't understand your request. Please try again.")
        return

    if output["intent"] == "chat":
        speak(output["message"])

    speak("Command received. Processing your request.")

    if output["intent"] == "add_task":
        result = add_task(output)
        speak(result)

    elif output["intent"] == "remove_task":
        result = remove_task(output)
        speak(result)

    elif output["intent"] == "record":
        record(output["s_file_name"], output["duration"], output["unit"])

    elif output["intent"] == "open_recordings_folder":
        speak(open_recordings_folder())

    elif output["intent"] == "list_tasks":
        result = list_tasks()
        speak(result)

    elif output["intent"] == "web_search":
        speak("Please wait as the web search is being performed.")
        web_search(output["query"])
        speak(f"Successfully searched this query.")


def wait_for_wake():
    while True:
        text = listen_once()
        if text and ("wake up" in text.lower() or "up" in text.lower() or "wakeup" in text.lower() or "wake" in text.lower()):
            return


def execute_jarvis():
    ask_user()
