from helper import get_llm_response
import os

# Herramientas disponibles
def search_tool(query):
    return f"(Resultado simulado para búsqueda: '{query}')"

def calculator_tool(expression):
    try:
        return str(eval(expression))
    except:
        return "Error en el cálculo"

# Historial del agente
history = []

# Loop del agente (pensar-actuar-observar)
def agent_loop(user_input):
    done = False
    while not done:
        print(f"\n🧠 Pregunta del usuario: {user_input}")
        
        # Crear el contexto (prompt completo)
        context = "\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in history])
        prompt = f"""
Eres un agente inteligente que puede usar herramientas.

Tienes disponibles estas herramientas:
1. calculator[expresión] → realiza cálculos matemáticos
2. search[pregunta] → simula una búsqueda online

Sigue este patrón:
- Pensar
- Acción: herramienta[entrada]
- Observación: resultado
- Repite si es necesario
- Final Answer: respuesta final

{context}
USER: {user_input}
AGENTE:"""

        reply = get_llm_response(prompt)
        print("🤖 Respuesta del agente:\n", reply)
        
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": reply})
        
        # Manejar acciones
        if "Final Answer:" in reply:
            done = True
        elif "Action: search" in reply:
            try:
                query = reply.split("search[")[1].split("]")[0]
                result = search_tool(query)
                print("🔍 Resultado:", result)
                user_input = f"Observation: {result}"
            except:
                print("❌ Error al procesar search")
                done = True
        elif "Action: calculator" in reply:
            try:
                expression = reply.split("calculator[")[1].split("]")[0]
                result = calculator_tool(expression)
                print("🧮 Resultado:", result)
                user_input = f"Observation: {result}"
            except:
                print("❌ Error al procesar cálculo")
                done = True
        else:
            done = True

# Ejecutar prueba
if __name__ == "__main__":
    pregunta = input("🗣️ ¿Qué deseas preguntarle al agente?: ")
    agent_loop(pregunta)
