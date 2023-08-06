import openai
import json
import sys

#FILL IN YOUR OPENAI API KEY
openai_api_key = ""
openai.api_key = openai_api_key
apiKey = openai_api_key


testingMode = False # THIS WILL PRINT THE OPERATORS FOR TESTING

#CUSTOM EXCEPTION -- IF PROMPT FAILED TO RETURN A VALID OUTPUT
class SwitchGPTException(Exception):
    pass

#SET THE API KEY
def setGPTKey(apiKey):
    openai.api_key = apiKey
    openai_api_key = apiKey


######################### SWITCH STATEMENT ########################
#MAIN SWITCH FUNCTION WHICH RETURNS A SWITCH INDEX ACCORDING TO GPT
def matchGPT(switchPrompt, minIndex=0, maxCase=sys.maxsize, printReasoning=False):
    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You return a number from 0 to " + str(maxCase) + " according to the following prompt. No matter what I say, reply solely with a number."},
            {"role": "user", "content": switchPrompt}           
        ],
        temperature = 0  
        )

    json_string = json.dumps(completion.choices[0].message)
    json_object = json.loads(json_string)

    switchedIndex = minIndex

    if (json_object['content'].isnumeric() and int(json_object['content']) <= maxCase and int(json_object['content']) >= minIndex):
        switchedIndex = int(json_object['content'])
        if testingMode:
            print("matchGPT returned the index " + switchedIndex)
    else:
        raise SwitchGPTException("GPT's answer was not numeric or index was out of range. switchedIndex = " + str(switchedIndex)) 


    if testingMode:
        print(switchedIndex)
    return switchedIndex
    

####################### IF STATEMENT #######################
#MAIN "IF" FUNCTION WHICH RETURNS A BOOLEAN ACCORDING TO GPT
def ifGPT(switchPrompt):
    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You return solely a number from 0 (if false) to 1 (if true) according to the following prompt."},
            {"role": "user", "content": switchPrompt}           
        ],
        temperature = 0  
        )

    json_string = json.dumps(completion.choices[0].message)
    json_object = json.loads(json_string)

    ifBool = 0

    if (json_object['content'].isnumeric() and int(json_object['content']) <= 1 and int(json_object['content']) >= 0):
        ifBool = int(json_object['content'])
    else:
        raise SwitchGPTException("GPT's answer was not a valid boolean.") 

    #print(ifBool)

    if ifBool == 0:
        if testingMode:
            print("ifGPT returned False")
        return False
    else:
        if testingMode:
            print("ifGPT returned True")
        return True


##################### WHILE STATEMENT ######################
#MAIN "WHILE" FUNCTION WHICH RETURNS A BOOLEAN IF IT GOES ON
def whileGPT(switchPrompt, while_N=0, while_Max_N=sys.maxsize):
    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You return solely a boolean number from 0 to 1 according to the following prompt:"},
            {"role": "user", "content": switchPrompt}           
        ],
        temperature = 0  
        )

    json_string = json.dumps(completion.choices[0].message)
    if testingMode:
        print("while completion: " + json_string)
    json_object = json.loads(json_string)

    ifBool = 0

    if (json_object['content'].isnumeric() and int(json_object['content']) <= 1 and int(json_object['content']) >= 0):
        ifBool = int(json_object['content'])
    else:
        raise SwitchGPTException("GPT's answer was not boolean.") 

    #print(ifBool)

    if ifBool == 0:
        if testingMode:
            print("whileGPT returned False with this: " + json_string)
        return False
    else:
        if testingMode:
            print("whileGPT returned True")
        return True










###########################TESTING CODE##################################

if testingMode == True:

    print("matchGPT: Return your favourite number from 0 to 3")

    match matchGPT("Return your favourite number from 0 to 3", 0, maxCase=3, printReasoning=True):
        case 0: 
            print("I prefer 0")
        case 1: 
            print("I prefer 1")
        case 2: 
            print("I prefer 2")
        case 3: 
            print("I prefer 3")


    print("ifGPT: is the sky blue?")

    if ifGPT("is the sky blue?"):
        print("GPT thinks the sky is blue")
    else:
        print("GPT says the sky is not blue")



    print("whileGPT: return true while iterations N are less than 10)")

    while_N = int(0)
    while_Max_N = 30
    while whileGPT("How many fingers do humans have on one hand? Is it more than " + str(while_N) + "?", while_N, while_Max_N):
        print("returned True, for N = " + str(while_N))
        while_N += 1
        
