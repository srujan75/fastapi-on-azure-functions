import fastapi
import random

app = fastapi.FastAPI()

# Route 1: Fun Welcome Message
@app.get("/sample")
async def index():
    return {
        "info": "Welcome to my FastAPI playground! Try /hello/yourname or /joke for fun. 🎈",
    }

# Route 2: Personalized Greeting
@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "message": f"Hey {name}! You're awesome! 🚀",
    }

# Route 3: Fun Fact Route
@app.get("/funfact")
async def fun_fact():
    return {
        "fact": "Did you know? Honey never spoils! 🍯",
    }

# Route 4: Visit Counter
visit_count = 0

@app.get("/visits")
async def count_visits():
    global visit_count
    visit_count += 1
    return {"message": f"You have visited {visit_count} times! 🎉"}

# Route 5: Random Joke Generator
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts! 💀",
    "What do you call fake spaghetti? An impasta! 🍝",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"
]

@app.get("/joke")
async def random_joke():
    return {"joke": random.choice(jokes)}
