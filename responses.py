import random

def sendResponse(user_input, user_name):
    user_input = user_input.lower()

    # Handle greetings
    greetings = ["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "g’day", "howdy"]
    if user_input in greetings:
        chosen_greeting = random.randint(1,5)
        off_chance = random.randint(1,100)
        match chosen_greeting:
                case 1:
                    if off_chance == 100:
                        return "It's a beutiful day outside..."
                    return f"Hi there {user_name}."
                case 2:
                    if off_chance == 100:
                        return"Birds are singing..."
                    return f"Hola {user_name}!"
                case 3:
                    if off_chance == 100:
                        return"Flowers are blooming..."
                    return f"Greetings {user_name}."
                case 4:
                    if off_chance == 100:
                        return"On days like these..."
                    return f"Hello {user_name}."
                case 5:
                    if off_chance == 100:
                        return"Kids like you..."
                    return f"Nice to meet you {user_name}!"
    else:
        return"I'm not sure of that greeting..."
