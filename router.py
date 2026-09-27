import subprocess
import datetime
import platform
import webbrowser
import os


def handle_local_command(command):
    """
    Handles commands that can be performed directly
    on the user's computer.

    Returns:
        str: Vali's response if handled locally.
        None: Send command to AI brain.
    """

    command = command.lower().strip()

    # =========================
    # TIME
    # =========================

    if (
        "what time is it" in command
        or "what's the time" in command
        or "tell me the time" in command
        or command == "time"
    ):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # =========================
    # DATE
    # =========================

    if (
        "what is today's date" in command
        or "what's today's date" in command
        or "what is the date" in command
        or "tell me the date" in command
        or command == "date"
    ):
        current_date = datetime.datetime.now().strftime(
            "%A, %d %B %Y"
        )
        return f"Today is {current_date}."

    # =========================
    # CALCULATOR
    # =========================

    if any(phrase in command for phrase in [
        "open calculator",
        "opening calculator",
        "launch calculator",
        "start calculator",
        "open calc",
        "launch calc"
    ]):
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    # =========================
    # NOTEPAD
    # =========================

    if any(phrase in command for phrase in [
        "open notepad",
        "opening notepad",
        "launch notepad",
        "start notepad"
    ]):
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    # =========================
    # FILE EXPLORER
    # =========================

    if any(phrase in command for phrase in [
        "open file explorer",
        "opening file explorer",
        "launch file explorer",
        "open explorer",
        "opening explorer",
        "launch explorer"
    ]):
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer."

    # =========================
    # TASK MANAGER
    # =========================

    if any(phrase in command for phrase in [
        "open task manager",
        "opening task manager",
        "launch task manager",
        "start task manager"
    ]):
        subprocess.Popen("taskmgr.exe")
        return "Opening Task Manager."

    # =========================
    # CHROME
    # =========================

    if any(phrase in command for phrase in [
        "open chrome",
        "opening chrome",
        "launch chrome",
        "start chrome"
    ]):
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        for path in chrome_paths:

            if os.path.exists(path):
                subprocess.Popen(path)
                return "Opening Google Chrome."

        return "I couldn't find Google Chrome."

    # =========================
    # VS CODE
    # =========================

    if any(phrase in command for phrase in [
        "open vscode",
        "open vs code",
        "opening vscode",
        "opening vs code",
        "launch vscode",
        "launch vs code",
        "start vscode",
        "start vs code"
    ]):
        try:
            subprocess.Popen("code")
            return "Opening Visual Studio Code."

        except FileNotFoundError:
            return "I couldn't find Visual Studio Code."

    # =========================
    # WEBSITES
    # =========================

    if any(phrase in command for phrase in [
        "open youtube",
        "opening youtube",
        "launch youtube",
        "start youtube"
    ]):
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    if any(phrase in command for phrase in [
        "open google",
        "opening google",
        "launch google",
        "start google"
    ]):
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    if any(phrase in command for phrase in [
        "open github",
        "opening github",
        "launch github",
        "start github"
    ]):
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    if any(phrase in command for phrase in [
        "open gmail",
        "opening gmail",
        "launch gmail",
        "start gmail"
    ]):
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    # =========================
    # FOLDERS
    # =========================

    if any(phrase in command for phrase in [
        "open downloads",
        "opening downloads",
        "launch downloads"
    ]):
        subprocess.Popen(
            ["explorer.exe", "shell:Downloads"]
        )
        return "Opening Downloads."

    if any(phrase in command for phrase in [
        "open documents",
        "opening documents",
        "launch documents"
    ]):
        subprocess.Popen(
            ["explorer.exe", "shell:Personal"]
        )
        return "Opening Documents."

    if any(phrase in command for phrase in [
        "open desktop",
        "opening desktop",
        "launch desktop"
    ]):
        subprocess.Popen(
            ["explorer.exe", "shell:Desktop"]
        )
        return "Opening Desktop."

    # =========================
    # SYSTEM STATUS
    # =========================

    if any(phrase in command for phrase in [
        "system status",
        "system information",
        "computer status",
        "computer information"
    ]):
        computer = platform.system()
        release = platform.release()
        machine = platform.machine()

        return (
            f"System: {computer} {release}. "
            f"Architecture: {machine}."
        )

    # =========================
    # NO LOCAL COMMAND
    # =========================

    return None