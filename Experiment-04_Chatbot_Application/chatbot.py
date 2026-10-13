"""
EXPERIMENT 4: Designing a Chat-bot Application
Course: AI Lab Practical (CSE)
Description:
    Rule-based Natural Language Processing (NLP) Chatbot with Intent Classification,
    keyword pattern matching, fallback responses, and interactive dialogue management.
"""

import re
import random
import sys


class AIChatbot:
    def __init__(self, bot_name="Nova"):
        self.bot_name = bot_name
        self.intents = self._build_knowledge_base()

    def _build_knowledge_base(self):
        """
        Build Knowledge Base of Intents with associated patterns and responses.
        """
        return [
            {
                "tag": "greeting",
                "patterns": [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"good (morning|afternoon|evening)"],
                "responses": [
                    f"Hello! I am {self.bot_name}, your AI Lab Assistant. How can I help you today?",
                    f"Hi there! Welcome to the AI Lab portal. What would you like to know?",
                    f"Greetings! {self.bot_name} here. Ask me anything about AI Lab experiments or schedules."
                ]
            },
            {
                "tag": "identity",
                "patterns": [r"who are you", r"what is your name", r"tell me about yourself"],
                "responses": [
                    f"I am {self.bot_name}, an AI Chatbot built using Python for the B.E. CSE AI Lab.",
                    f"My name is {self.bot_name}. I help students with lab experiments, algorithms, and practical queries."
                ]
            },
            {
                "tag": "experiments",
                "patterns": [r"experiment", r"syllabus", r"lab practical", r"list (of )?experiments"],
                "responses": [
                    "Here are the AI Lab experiments:\n"
                    "  Exp 1: Data Pre-processing & Annotation\n"
                    "  Exp 2: BFS and DFS Search Techniques\n"
                    "  Exp 3: Hill Climbing and A* Algorithm\n"
                    "  Exp 4: Chatbot Application Design\n"
                    "  Exp 5: Inference System (Forward/Backward Chaining)\n"
                    "  Exp 6: N-Queens Problem (N=1 to 9)"
                ]
            },
            {
                "tag": "search_algorithms",
                "patterns": [r"bfs", r"dfs", r"a\*", r"hill climbing", r"search"],
                "responses": [
                    "BFS explores level-by-level using a Queue (O(b^d)).\n"
                    "DFS explores branch-by-branch using a Stack (O(bm)).\n"
                    "A* combines actual cost g(n) and heuristic h(n) to find the optimal path!\n"
                    "Hill Climbing moves in the direction of increasing heuristic value."
                ]
            },
            {
                "tag": "n_queens",
                "patterns": [r"n-?queens?", r"queen problem", r"backtracking"],
                "responses": [
                    "The N-Queens problem places N queens on an N x N chessboard such that\n"
                    "no two queens attack each other (same row, column, or diagonal).\n"
                    "It is solved using Backtracking with constraint checks."
                ]
            },
            {
                "tag": "lab_timings",
                "patterns": [r"timing", r"hours", r"schedule", r"when is lab"],
                "responses": [
                    "Each AI Lab experiment is allocated 5 hours, totaling 75 hours for the course.",
                    "AI practical sessions are scheduled according to the department timetable."
                ]
            },
            {
                "tag": "thanks",
                "patterns": [r"thank you", r"thanks", r"appreciate it", r"great job"],
                "responses": [
                    "You're very welcome! Happy coding!",
                    "Glad I could help! Good luck with your AI practicals!",
                    "Anytime! Feel free to ask if you need further assistance."
                ]
            },
            {
                "tag": "goodbye",
                "patterns": [r"\bbye\b", r"\bexit\b", r"\bquit\b", r"see you", r"good night"],
                "responses": [
                    f"Goodbye! Have a productive lab session!",
                    f"See you next time! Don't forget to submit your record notebook!",
                    f"Bye! Best of luck in your AI practical exam!"
                ]
            }
        ]

    def clean_text(self, text):
        """Preprocesses user input by lowercasing and removing punctuation."""
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]", "", text)
        return text

    def get_response(self, user_input):
        """
        Matches cleaned user input against intent patterns.
        Returns matched response and the identified intent tag.
        """
        cleaned = self.clean_text(user_input)

        if not cleaned:
            return "Please type something so I can help you!", "empty"

        for intent in self.intents:
            for pattern in intent["patterns"]:
                if re.search(pattern, cleaned):
                    # Deterministic pick for testing or random pick
                    response = random.choice(intent["responses"])
                    return response, intent["tag"]

        # Default Fallback Response
        fallback_responses = [
            "I'm sorry, I didn't quite understand that. Could you rephrase your question?",
            "I do not have information on that yet. You can ask me about AI Lab experiments, BFS/DFS, A*, or N-Queens!",
            "Could you please specify your query regarding the AI practical syllabus?"
        ]
        return random.choice(fallback_responses), "fallback"

    def chat_interactive(self):
        """Starts interactive conversation loop with the user."""
        print("=" * 70)
        print(f"WELCOME TO {self.bot_name.upper()} - AI LAB CONVERSATIONAL ASSISTANT")
        print("Type 'exit' or 'bye' to quit at any time.")
        print("=" * 70)

        while True:
            try:
                user_msg = input("\nYou: ")
            except (EOFError, KeyboardInterrupt):
                print(f"\n{self.bot_name}: Goodbye! Have a great day.")
                break

            response, tag = self.get_response(user_msg)
            print(f"{self.bot_name}: {response}")

            if tag == "goodbye":
                break

    def run_demo_simulation(self):
        """Runs an automated multi-turn conversation demo."""
        test_queries = [
            "Hello there!",
            "What is your name?",
            "Can you tell me the list of experiments?",
            "Explain BFS and DFS search algorithms",
            "What is the N-Queens problem?",
            "What are the lab timings?",
            "What is the weather outside?",
            "Thank you so much!",
            "Bye"
        ]

        print("=" * 70)
        print(f"AUTOMATED CONVERSATION SIMULATION: {self.bot_name.upper()}")
        print("=" * 70)

        for query in test_queries:
            print(f"\nUser : {query}")
            response, tag = self.get_response(query)
            print(f"{self.bot_name} [{tag.upper()}]:\n{response}")


def main():
    bot = AIChatbot(bot_name="Nova")
    # Check if run with --demo or non-interactive pipe
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        bot.chat_interactive()
    else:
        # Default runs simulation demo for reproducible lab output
        bot.run_demo_simulation()


if __name__ == "__main__":
    main()
