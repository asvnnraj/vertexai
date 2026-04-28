import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.vertex_llm import ask_llm, get_embedding

print(ask_llm("Explain why gold is a hedge against inflation in 3 lines"))

vec = get_embedding("customer prefers low risk investments")
print(len(vec))
