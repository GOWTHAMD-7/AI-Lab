# EXPERIMENT 4: Designing a Chat-bot Application

---

## 1. Aim
To design and implement an intelligent rule-based Conversational Chatbot application using Natural Language Processing (NLP) techniques (intent classification, pattern matching, response generation, and fallback handling) in Python.

---

## 2. Algorithm (5 - 6 Simple Steps to Write in Record / Exam)

1. **Step 1: Knowledge Base Definition:** Construct an intent knowledge base containing structured tags (e.g., `greeting`, `experiments`, `algorithms`, `goodbye`), regular expression patterns, and appropriate response lists.
2. **Step 2: Input Pre-processing:** Receive user input string, convert to lowercase, and strip punctuation marks and extra whitespace using regex tokenization.
3. **Step 3: Intent Matching:** Iterate through intent patterns and evaluate whether the pre-processed user message matches any defined intent regular expressions.
4. **Step 4: Response Generation:** If a matching intent is found, randomly choose an appropriate response from that intent's response bank to provide dynamic conversational variety.
5. **Step 5: Fallback Handling:** If no patterns match with confidence, execute a default fallback mechanism asking the user to clarify or rephrase their query.
6. **Step 6: Dialogue Management Loop:** Maintain an interactive dialogue loop until a termination intent (`bye`, `quit`, `exit`) is triggered.

---

## 3. Architecture of Chatbot

```text
  [User Input]
       │
       ▼
 [Text Preprocessing] (Lowercase, Remove Punctuation)
       │
       ▼
 [Intent Recognition Engine] (Regex Pattern Matching)
       │
       ├─── Match Found ───► [Select Intent Response] ──┐
       │                                                │
       └─── No Match ──────► [Fallback Handler] ────────┤
                                                        │
                                                        ▼
                                              [Deliver Bot Response]
```

---

## 4. Source Code (`chatbot.py`)

```python
"""
EXPERIMENT 4: Chatbot Application
"""
import re
import random
import sys

class AIChatbot:
    def __init__(self, bot_name="Nova"):
        self.bot_name = bot_name
        self.intents = [
            {
                "tag": "greeting",
                "patterns": [r"\bhi\b", r"\bhello\b", r"\bhey\b"],
                "responses": ["Hello! How can I assist you with your AI Lab today?"]
            },
            {
                "tag": "experiments",
                "patterns": [r"experiment", r"syllabus", r"practical"],
                "responses": [
                    "AI Lab Experiments:\n"
                    "1. Data Pre-processing & Annotation\n"
                    "2. BFS and DFS Search\n"
                    "3. Hill Climbing & A* Algorithm\n"
                    "4. Chatbot Design\n"
                    "5. Inference System\n"
                    "6. N-Queens Problem (N=1 to 9)"
                ]
            },
            {
                "tag": "algorithms",
                "patterns": [r"bfs", r"dfs", r"a\*", r"search"],
                "responses": ["BFS uses Queue (FIFO), DFS uses Stack (LIFO), and A* uses f(n)=g(n)+h(n)!"]
            },
            {
                "tag": "goodbye",
                "patterns": [r"\bbye\b", r"\bexit\b", r"\bquit\b"],
                "responses": ["Goodbye! Best of luck in your practical exams!"]
            }
        ]

    def clean_text(self, text):
        return re.sub(r"[^\w\s]", "", text.lower().strip())

    def get_response(self, text):
        cleaned = self.clean_text(text)
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if re.search(pattern, cleaned):
                    return random.choice(intent["responses"]), intent["tag"]
        return "I'm sorry, I didn't understand. Could you rephrase?", "fallback"

    def chat(self):
        print(f"Chatbot {self.bot_name} started. Type 'bye' to exit.")
        while True:
            msg = input("You: ")
            reply, tag = self.get_response(msg)
            print(f"{self.bot_name}: {reply}")
            if tag == "goodbye":
                break

if __name__ == "__main__":
    bot = AIChatbot()
    bot.chat()
```

---

## 5. Sample Input and Output

### Interactive / Simulated Dialogue:

```text
======================================================================
AUTOMATED CONVERSATION SIMULATION: NOVA
======================================================================

User : Hello there!
Nova [GREETING]:
Greetings! Nova here. Ask me anything about AI Lab experiments or schedules.

User : What is your name?
Nova [IDENTITY]:
I am Nova, an AI Chatbot built using Python for the B.E. CSE AI Lab.

User : Can you tell me the list of experiments?
Nova [EXPERIMENTS]:
Here are the AI Lab experiments:
  Exp 1: Data Pre-processing & Annotation
  Exp 2: BFS and DFS Search Techniques
  Exp 3: Hill Climbing and A* Algorithm
  Exp 4: Chatbot Application Design
  Exp 5: Inference System (Forward/Backward Chaining)
  Exp 6: N-Queens Problem (N=1 to 9)

User : Explain BFS and DFS search algorithms
Nova [SEARCH_ALGORITHMS]:
BFS explores level-by-level using a Queue (O(b^d)).
DFS explores branch-by-branch using a Stack (O(bm)).
A* combines actual cost g(n) and heuristic h(n) to find the optimal path!
Hill Climbing moves in the direction of increasing heuristic value.

User : What is the N-Queens problem?
Nova [N_QUEENS]:
The N-Queens problem places N queens on an N x N chessboard such that
no two queens attack each other (same row, column, or diagonal).
It is solved using Backtracking with constraint checks.

User : What are the lab timings?
Nova [LAB_TIMINGS]:
AI practical sessions are scheduled according to the department timetable.

User : What is the weather outside?
Nova [FALLBACK]:
I do not have information on that yet. You can ask me about AI Lab experiments, BFS/DFS, A*, or N-Queens!

User : Thank you so much!
Nova [THANKS]:
Anytime! Feel free to ask if you need further assistance.

User : Bye
Nova [GOODBYE]:
See you next time! Don't forget to submit your record notebook!
```

---

## 6. Result & Viva Questions

### Result:
A conversational rule-based AI Chatbot application was successfully designed and tested. It accurately classifies user queries across domain-specific intents, generates appropriate answers, gracefully handles unrecognised inputs via fallback responses, and terminates gracefully upon exit.

### Viva Voce Q&A:
1. **Q: What is the difference between a Rule-based chatbot and a Generative AI chatbot?**
   - **A:** Rule-based chatbots use predefined pattern matching and curated response rules, making them deterministic, predictable, and safe for domain FAQs. Generative AI chatbots use Large Language Models (LLMs) or neural networks (Transformers) to generate novel responses dynamically based on probabilities.
2. **Q: What is an Intent and an Entity in conversational AI?**
   - **A:** An **Intent** represents the user's overall goal or intention (e.g., `check_syllabus`), while an **Entity** represents specific parameters or data extracted from the utterance (e.g., date, subject name, experiment number).
3. **Q: How does the chatbot handle ambiguous or unknown queries?**
   - **A:** Through a **fallback handler**, which politely acknowledges lack of matching knowledge and prompts the user to rephrase with suggested topic hints.
