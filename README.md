
---

# GPT-Branching-Operators

Leverage the intelligence of GPT models within your Python scripts using the GPT-Branching-Operators package. Integrate natural language processing into your decision-making processes, allowing for more human-like and contextual logic flow in your applications. It is now available and functional for the branching "ifGPT", "matchGPT", and "whileGPT".

## Prerequisites

- Python 3.x
- OpenAI API Key

### Installation

To install the required dependencies, run the following command:

```bash
pip3 install openai json sys
```

## Quick Start

Here's how you can quickly get started with GPT-Branching-Operators:

1. **Import the package:**

```python
from GPT_Operators import *
```

2. **Set your OpenAI API Key:**

```python
setGPTKey("sk-ZZZ...")
```

Replace `"sk-ZZZ..."` with your actual OpenAI API key.

3. **Use the GPT branching operator in your logic:**

```python
if ifGPT("Is the sky blue?"):
    print("Yep, the sky is blue.")
else:
    print("What?")
```

### Output:

```
Yep, the sky is blue
```


## License

This project is licensed under the MIT License. See the [LICENSE.md](<link-to-license-file>) file for details.


---

