"""
EXPERIMENT 5: Implementation of Inference System
Course: AI Lab Practical (CSE)
Description:
    Implements a Rule-Based Expert Inference Engine supporting both:
    1. Forward Chaining (Data-Driven Reasoning)
    2. Backward Chaining (Goal-Driven Reasoning)
    with trace logging and fact derivation.
"""


class Rule:
    def __init__(self, rule_id, premises, conclusion):
        self.rule_id = rule_id
        self.premises = set(premises)
        self.conclusion = conclusion

    def __repr__(self):
        return f"{self.rule_id}: IF {' AND '.join(sorted(self.premises))} THEN {self.conclusion}"


class InferenceEngine:
    def __init__(self, rules, initial_facts):
        self.rules = rules
        self.initial_facts = set(initial_facts)

    # ------------------------------------------------------------------
    # 1. FORWARD CHAINING (Data-Driven)
    # ------------------------------------------------------------------
    def forward_chaining(self, goal=None):
        """
        Forward Chaining: Starts with known facts and repeatedly applies
        rules whose premises are satisfied until no new facts are deduced
        or the target goal is derived.
        """
        known_facts = set(self.initial_facts)
        fired_rules = []
        iteration = 0

        print("\n" + "-" * 70)
        print("FORWARD CHAINING REASONING TRACE:")
        print("-" * 70)
        print(f"Initial Working Facts: {sorted(list(known_facts))}")

        while True:
            iteration += 1
            new_fact_derived = False

            for rule in self.rules:
                # If rule hasn't fired yet and all premises exist in known facts
                if rule not in fired_rules and rule.premises.issubset(known_facts):
                    if rule.conclusion not in known_facts:
                        known_facts.add(rule.conclusion)
                        fired_rules.append(rule)
                        new_fact_derived = True
                        print(f"  [Fire {rule.rule_id}] Premises met: {sorted(list(rule.premises))}")
                        print(f"               -> Derived New Fact: '{rule.conclusion}'")

                        if goal and rule.conclusion == goal:
                            print(f"\nTarget Goal '{goal}' successfully derived!")
                            return True, known_facts, fired_rules

            if not new_fact_derived:
                break

        goal_status = (goal in known_facts) if goal else None
        return goal_status, known_facts, fired_rules

    # ------------------------------------------------------------------
    # 2. BACKWARD CHAINING (Goal-Driven)
    # ------------------------------------------------------------------
    def backward_chaining(self, goal, known_facts=None, visited=None, depth=0):
        """
        Backward Chaining: Starts with a goal and works backward to check
        if the goal can be satisfied by known facts or premise sub-goals.
        """
        indent = "  " * depth
        if known_facts is None:
            known_facts = set(self.initial_facts)
        if visited is None:
            visited = set()

        print(f"{indent}? Testing Goal / Sub-goal: '{goal}'")

        # Base case 1: Goal is already a known fact
        if goal in known_facts:
            print(f"{indent}  => TRUE: '{goal}' is directly present in Known Facts database.")
            return True

        if goal in visited:
            print(f"{indent}  => Cycle detected for '{goal}'. Returning False.")
            return False
        visited.add(goal)

        # Base case 2: Find candidate rules whose conclusion is the goal
        matching_rules = [r for r in self.rules if r.conclusion == goal]
        if not matching_rules:
            print(f"{indent}  => FALSE: No rules found that conclude '{goal}'.")
            return False

        for rule in matching_rules:
            print(f"{indent}  Checking candidate rule {rule.rule_id}: IF {' AND '.join(sorted(rule.premises))} THEN {goal}")
            all_premises_proven = True

            for premise in sorted(list(rule.premises)):
                # Recursively check premise as a sub-goal
                if not self.backward_chaining(premise, known_facts, visited.copy(), depth + 1):
                    all_premises_proven = False
                    break

            if all_premises_proven:
                print(f"{indent}  => SUCCESS: All premises for {rule.rule_id} proven. Conclude '{goal}' is TRUE.")
                known_facts.add(goal)
                return True

        print(f"{indent}  => FAILED: Could not prove goal '{goal}' through candidate rules.")
        return False


def run_experiment():
    print("=" * 70)
    print("EXPERIMENT 5: IMPLEMENTATION OF INFERENCE SYSTEM")
    print("=" * 70)

    # Define Domain Rules for Expert Medical Diagnosis Knowledge Base
    rules = [
        Rule("R1", ["fever", "cough"], "infection"),
        Rule("R2", ["infection", "sore_throat"], "influenza"),
        Rule("R3", ["infection", "loss_of_smell"], "covid19"),
        Rule("R4", ["fever", "rash"], "measles"),
        Rule("R5", ["influenza"], "prescribe_antiviral_and_rest"),
        Rule("R6", ["covid19"], "prescribe_isolation_and_oxygen")
    ]

    initial_facts = ["fever", "cough", "sore_throat"]
    target_goal = "prescribe_antiviral_and_rest"

    print("\nKNOWLEDGE BASE (RULE BASE):")
    for r in rules:
        print(f"  {r}")

    print(f"\nINITIAL FACTS IN WORKING MEMORY: {initial_facts}")
    print(f"TARGET GOAL TO PROVE: '{target_goal}'")

    engine = InferenceEngine(rules, initial_facts)

    # 1. Forward Chaining Test
    print("\n" + "=" * 70)
    print("1. FORWARD CHAINING INFERENCE (DATA-DRIVEN)")
    print("=" * 70)
    goal_found, final_facts, fired_rules = engine.forward_chaining(goal=target_goal)

    print("\nForward Chaining Summary:")
    print(f"  Rules Fired     : {[r.rule_id for r in fired_rules]}")
    print(f"  All Known Facts : {sorted(list(final_facts))}")
    print(f"  Goal Verified   : {goal_found} ('{target_goal}')")

    # 2. Backward Chaining Test
    print("\n" + "=" * 70)
    print("2. BACKWARD CHAINING INFERENCE (GOAL-DRIVEN)")
    print("=" * 70)
    print(f"Hypothesis Goal to verify: '{target_goal}'\n")
    is_proven = engine.backward_chaining(goal=target_goal)

    print("\nBackward Chaining Summary:")
    print(f"  Goal Hypothesis : '{target_goal}'")
    print(f"  Verification    : {'PROVEN (TRUE)' if is_proven else 'DISPROVEN (FALSE)'}")
    print("=" * 70)


if __name__ == "__main__":
    run_experiment()
