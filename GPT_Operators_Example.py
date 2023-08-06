#from GPT_Operators import *
from GPT_Operators import *
setGPTKey("sk-...") ### THIS IS WHERE YOU PROVIDE THE API KEY FROM OPENAI >>> https://platform.openai.com/account/api-keys






if ifGPT("Is the sky blue?"):
    print("Yep, the sky is blue.")
else:
    print("What?")





match matchGPT("the first prime number"):
    case 0:
        print("You're wrong, 0 is not prime.")
    case 1:
        print("You're wrong, 1 is not prime.")
    case 2:
        print("You're correct, 2 is the first prime.")
    



while_N = int(0)
while_Max_N = 30
while whileGPT("How many fingers do humans have on one hand? Is it more than " + str(while_N) + "?", while_N, while_Max_N):
    print("returned True, for N = " + str(while_N))
    while_N += 1

