# GPT-Branching-Operators <br>
Use GPT as a branching operator within any of your python scripts <br>
 <br>
I am still a CompSci student so the code is not very polished, but it is a proof-of-concept that you can (and should) use GPT for any of your programming logic. <br>
 <br>
 <br>
from GPT_Operators import * <br>
setGPTKey("sk-ZZZ...") ### You need to provide the API Key from OpenAI <br>
 <br>
if ifGPT("Is the sky blue?"): <br>
&nbsp;&nbsp;&nbsp;&nbsp;print("Yep, the sky is blue.") <br>
else: <br>
&nbsp;&nbsp;&nbsp;&nbsp;print("What?") <br>
 <br>
Output: <b>Yep, the sky is blue <br></b>
