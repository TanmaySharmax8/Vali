# =========================
# VALI - VERSION 0.6.1
# Wake Word + Voice Assistant
# =========================

from brain import ask_vali
from router import handle_local_command
from voice import listen, speak
from wake_word import wait_for_wake_word


# =========================
# MAIN VALI SYSTEM
# =========================

def main():

    print("=" * 50)
    print("                 VALI")
    print("          Personal AI Assistant")
    print("=" * 50)
    print()

    print("Vali: Systems online.")
    print("Vali: Wake-word system ready.")
    print()

    speak("Systems online. Wake word system ready.")

    # =========================
    # MAIN LOOP
    # =========================

    while True:

        try:

            # Wait until user says "Hey Vali"
            wait_for_wake_word()

            # Vali has been activated
            speak("Yes?")

            # Listen for the actual command
            command = listen()

        except KeyboardInterrupt:

            print()
            print("Vali: Shutting down.")
            speak("Shutting down.")
            break

        except Exception as error:

            print()
            print("Voice error:", error)
            print()

            speak(
                "I am having trouble with my voice system."
            )

            continue

        # =========================
        # EMPTY COMMAND
        # =========================

        if not command:
            continue

        print("You:", command)

        command_lower = command.lower().strip()

        # =========================
        # SHUTDOWN
        # =========================

        if command_lower in [
            "exit",
            "quit",
            "shutdown",
            "shut down",
            "goodbye"
        ]:

            print("Vali: Shutting down. Goodbye.")

            speak(
                "Shutting down. Goodbye."
            )

            break

        # =========================
        # LOCAL COMMAND ROUTER
        # =========================

        local_response = handle_local_command(command)

        if local_response is not None:

            print("Vali:", local_response)

            speak(local_response)

            continue

        # =========================
        # ONLINE AI BRAIN
        # =========================

        print("Vali: Thinking...")

        try:

            answer = ask_vali(command)

            print("Vali:", answer)

            speak(answer)

        except Exception as error:

            print()
            print("Vali: Online AI brain unavailable.")
            print("Reason:", error)
            print()

            speak(
                "I can't reach my online brain right now. "
                "Please check the AI service."
            )


# =========================
# START VALI
# =========================

if __name__ == "__main__":

    main()