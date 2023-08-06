# GPT-Branching-Operators
Use GPT as a branching operator within any of your python scripts

I am still a CompSci student so the code is not very polished, but it is a proof-of-concept that you can (and should) use GPT for any of your programming logic.


from GPT_Operators import *
setGPTKey("sk-ZZZ...") ### You need to provide the API Key from OpenAI

if ifGPT("Is the sky blue?"):
    print("Yep, the sky is blue.")
else:
    print("What?")


Output: Yep, the sky is blue
