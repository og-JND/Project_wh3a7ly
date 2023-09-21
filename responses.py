import random

def sendResponse(user_input):
    user_input = user_input.lower()

    # Handle greetings
    greetings = ["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "g’day", "howdy"]
    if user_input in greetings:
        chosen_greeting = random.randint(1,5)
        off_chance = random.randint(1,100)
        if chosen_greeting == 1:
            if off_chance == 100:
                print("It's a beutiful day outside...")
            print("Hi there!")
        if chosen_greeting == 2:
            if off_chance == 100:
                print("Birds are singing...")
            print("Hola!")
        if chosen_greeting == 3:
            if off_chance == 100:
                print("Flowers are blooming...")
            print("Greetings!")
        if chosen_greeting == 4:
            if off_chance == 100:
                print("On days like these...")
            print("Hello.")
        if chosen_greeting == 5:
            if off_chance == 100:
                print("Kids like you...")
            print("Nice to meet you.")
        print(chosen_greeting)

