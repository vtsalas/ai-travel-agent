import os
import requests
from smolagents import CodeAgent, OpenAIServerModel, tool, DuckDuckGoSearchTool

# Το εργαλείο μας για τον καιρό
@tool
def get_weather(location: str) -> str:
    """
    Επιστρέφει τον τρέχοντα καιρό και τη θερμοκρασία για μια συγκεκριμένη τοποθεσία.
    
    Args:
        location: Το όνομα της πόλης (π.χ. 'London', 'Athens', 'Paris').
    """
    url = f"https://wttr.in/{location}?format=j1"
    
    try:
        # ΠΡΟΣΘΗΚΗ 1: Βάζουμε timeout=10. Αν αργήσει το API πάνω από 10 δευτερόλεπτα, 
        # αποτυγχάνει γρήγορα (Fail Fast) για να μπορέσει ο Agent να ψάξει στο ίντερνετ.
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        data = response.json()
        
        temp = data['current_condition'][0]['temp_C']
        description = data['current_condition'][0]['weatherDesc'][0]['value']
        
        return f"Ο καιρός στην περιοχή {location} είναι: {description} με θερμοκρασία {temp}°C."
    except Exception as e:
        return f"Σφάλμα: Δεν μπόρεσα να βρω τον καιρό μέσω του API. Παρακαλώ ψάξε στο ίντερνετ."

# Ρύθμιση του token της Hugging Face
os.environ["HUGGINGFACE_HUB_TOKEN"] = "your_token_here"

# Το μοντέλο μας
model = OpenAIServerModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    api_base="https://router.huggingface.co/v1",
    api_key=os.environ["HUGGINGFACE_HUB_TOKEN"]
)

# ΠΡΟΣΘΗΚΗ 2: Αρχικοποιούμε το εργαλείο αναζήτησης
search_tool = DuckDuckGoSearchTool()

# Δημιουργούμε τον CodeAgent και του δίνουμε ΚΑΙ τα δύο εργαλεία
agent = CodeAgent(
    tools=[get_weather, search_tool], # Τώρα έχει πρόσβαση και στο ίντερνετ!
    model=model,
    additional_authorized_imports=["requests", "json"]
)

# Το ανανεωμένο prompt μας
prompt = """
I'm flying to Norway this weekend for tourism. 
Find out what the weather is like there right now (if the weather API doesn't work, search the internet).
Then, based on the actual weather you found, make me a list of 5 
simple everyday things (clothes or accessories) that I absolutely must pack in my suitcase.
Give me the items with bullets on separated lines
Tell me the location and the degrees Celsius it is in a new line.
"""

print("Ο Agent σκέφτεται και ψάχνει... (Μπορεί να πάρει λίγο)\n")

# Εκτέλεση του agent
result = agent.run(prompt)

print("\n=== ΤΕΛΙΚΗ ΑΠΑΝΤΗΣΗ ===")
print(result)