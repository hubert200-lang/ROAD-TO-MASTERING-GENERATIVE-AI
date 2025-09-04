# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import environment_settings, connect_to_llm

environment_settings()
llm = connect_to_llm()
llm.invoke("Tell, me who is the GOAT, iLya suskever or Andrej Karpathy?")
print(llm)