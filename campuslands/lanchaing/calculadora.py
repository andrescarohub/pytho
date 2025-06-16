def search_tool(query):
    return f"(respuesta simulada para : {query})"


def calculator_tool(expresison):
    try:
        return str(eval(expresison))
    except:
        return "error de calculo"
    

import openai

openai.api_key = "TU_API_KEY"  # Reemplázala

# Simulamos la memoria del agente
history = []

def call_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # o el que tengas
        messages=[
            {"role": "system", "content": "Eres un agente que puede usar herramientas como 'search' y 'calculator'."},
            *history,
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def agent_loop(user_input):
    done = False
    while not done:
        print(f"\n🤔 Pensando con input: {user_input}")
        history.append({"role": "user", "content": user_input})
        reply = call_agent(user_input)
        print("🧠 Agente:", reply)
        history.append({"role": "assistant", "content": reply})
        
        if "Final Answer:" in reply:
            done = True
        elif "Action: search" in reply:
            # Extraer query
            query = reply.split("search[")[1].split("]")[0]
            result = search_tool(query)
            print("🔍 Resultado de search:", result)
            user_input = f"Observation: {result}"
        elif "Action: calculator" in reply:
            expression = reply.split("calculator[")[1].split("]")[0]
            result = calculator_tool(expression)
            print("🧮 Resultado del cálculo:", result)
            user_input = f"Observation: {result}"
        else:
            done = True

            agent_loop("¿Cuánto es (3 + 5) * 2?")

