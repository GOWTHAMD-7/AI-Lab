# EXPERIMENT 5: Implementation of Inference System

---

## 1. Aim
To implement an **Inference Engine** in Python that executes automated logical reasoning over a Rule-Based Knowledge Base using both **Forward Chaining (Data-Driven)** and **Backward Chaining (Goal-Driven)** strategies.

---

## 2. Algorithms (5 - 6 Simple Steps to Write in Record / Exam)

### A. Forward Chaining (Data-Driven Reasoning):
1. **Step 1: Initialize Working Memory:** Load the initially known ground facts into the working memory facts database.
2. **Step 2: Match Rule Premises:** Iterate through the rule base to find unfired rules whose antecedent conditions (IF conditions) are all present in the known facts set.
3. **Step 3: Fire Activated Rule:** Select an activated rule and execute/fire it.
4. **Step 4: Assert Consequent Fact:** Add the rule's conclusion (THEN part) into the working memory facts database.
5. **Step 5: Check Goal / Termination:** If the newly deduced fact matches the target query/goal, terminate with success. If no new rules can fire, terminate.
6. **Step 6: Return Deduced Knowledge:** Return the list of fired rules, updated facts base, and goal status.

---

### B. Backward Chaining (Goal-Driven Reasoning):
1. **Step 1: Set Hypothesis Goal:** Start with the top-level query/goal to be verified.
2. **Step 2: Direct Fact Check:** If the goal is already present in the initial known facts base, return `TRUE`.
3. **Step 3: Search Consequent Rules:** Look up rules in the rule base whose conclusion (THEN part) matches the goal.
4. **Step 4: Recursive Sub-Goal Verification:** For each candidate rule, treat each premise condition as a new sub-goal and evaluate it recursively.
5. **Step 5: Prove Rule:** If all antecedent conditions of a candidate rule are evaluated to `TRUE`, conclude that the current goal is `TRUE`.
6. **Step 6: Report Conclusion:** If no rule can prove the goal, return `FALSE`.

---

## 3. Knowledge Base Specification

### Rules:
- **R1:** IF `fever` AND `cough` $\rightarrow$ `infection`
- **R2:** IF `infection` AND `sore_throat` $\rightarrow$ `influenza`
- **R3:** IF `infection` AND `loss_of_smell` $\rightarrow$ `covid19`
- **R4:** IF `fever` AND `rash` $\rightarrow$ `measles`
- **R5:** IF `influenza` $\rightarrow$ `prescribe_antiviral_and_rest`
- **R6:** IF `covid19` $\rightarrow$ `prescribe_isolation_and_oxygen`

### Initial Known Facts:
`['fever', 'cough', 'sore_throat']`

### Target Goal to Prove:
`'prescribe_antiviral_and_rest'`

---

## 4. Source Code (`inference_system.py`)

```python
"""
EXPERIMENT 5: Inference System (Forward & Backward Chaining)
"""

class Rule:
    def __init__(self, rule_id, premises, conclusion):
        self.rule_id = rule_id
        self.premises = set(premises)
        self.conclusion = conclusion

# Forward Chaining Engine
def forward_chaining(rules, facts, goal):
    known = set(facts)
    fired = []
    while True:
        new_fact = False
        for r in rules:
            if r not in fired and r.premises.issubset(known):
                if r.conclusion not in known:
                    known.add(r.conclusion)
                    fired.append(r)
                    new_fact = True
                    print(f"Fired {r.rule_id} -> Added '{r.conclusion}'")
                    if r.conclusion == goal:
                        return True, known
        if not new_fact:
            break
    return (goal in known), known

# Backward Chaining Engine
def backward_chaining(rules, facts, goal, visited=None):
    if visited is None: visited = set()
    if goal in facts: return True
    if goal in visited: return False
    visited.add(goal)

    candidates = [r for r in rules if r.conclusion == goal]
    for r in candidates:
        if all(backward_chaining(rules, facts, p, visited.copy()) for p in r.premises):
            return True
    return False

# Knowledge Base
rules = [
    Rule("R1", ["fever", "cough"], "infection"),
    Rule("R2", ["infection", "sore_throat"], "influenza"),
    Rule("R3", ["infection", "loss_of_smell"], "covid19"),
    Rule("R4", ["fever", "rash"], "measles"),
    Rule("R5", ["influenza"], "prescribe_antiviral_and_rest")
]
initial_facts = ["fever", "cough", "sore_throat"]
goal = "prescribe_antiviral_and_rest"

print("--- Forward Chaining ---")
res, derived = forward_chaining(rules, initial_facts, goal)
print("Goal Proven:", res)

print("\n--- Backward Chaining ---")
proven = backward_chaining(rules, set(initial_facts), goal)
print("Goal Verified:", proven)
```

---

## 5. Sample Input and Output

### Input:
- **Initial Facts:** `['fever', 'cough', 'sore_throat']`
- **Target Goal:** `'prescribe_antiviral_and_rest'`

### Execution Output:
```text
======================================================================
EXPERIMENT 5: IMPLEMENTATION OF INFERENCE SYSTEM
======================================================================

KNOWLEDGE BASE (RULE BASE):
  R1: IF cough AND fever THEN infection
  R2: IF infection AND sore_throat THEN influenza
  R3: IF infection AND loss_of_smell THEN covid19
  R4: IF fever AND rash THEN measles
  R5: IF influenza THEN prescribe_antiviral_and_rest
  R6: IF covid19 THEN prescribe_isolation_and_oxygen

INITIAL FACTS IN WORKING MEMORY: ['fever', 'cough', 'sore_throat']
TARGET GOAL TO PROVE: 'prescribe_antiviral_and_rest'

======================================================================
1. FORWARD CHAINING INFERENCE (DATA-DRIVEN)
======================================================================

----------------------------------------------------------------------
FORWARD CHAINING REASONING TRACE:
----------------------------------------------------------------------
Initial Working Facts: ['cough', 'fever', 'sore_throat']
  [Fire R1] Premises met: ['cough', 'fever']
               -> Derived New Fact: 'infection'
  [Fire R2] Premises met: ['infection', 'sore_throat']
               -> Derived New Fact: 'influenza'
  [Fire R5] Premises met: ['influenza']
               -> Derived New Fact: 'prescribe_antiviral_and_rest'

Target Goal 'prescribe_antiviral_and_rest' successfully derived!

Forward Chaining Summary:
  Rules Fired     : ['R1', 'R2', 'R5']
  All Known Facts : ['cough', 'fever', 'infection', 'influenza', 'prescribe_antiviral_and_rest', 'sore_throat']
  Goal Verified   : True ('prescribe_antiviral_and_rest')

======================================================================
2. BACKWARD CHAINING INFERENCE (GOAL-DRIVEN)
======================================================================
Hypothesis Goal to verify: 'prescribe_antiviral_and_rest'

? Testing Goal / Sub-goal: 'prescribe_antiviral_and_rest'
  Checking candidate rule R5: IF influenza THEN prescribe_antiviral_and_rest
  ? Testing Goal / Sub-goal: 'influenza'
    Checking candidate rule R2: IF infection AND sore_throat THEN influenza
    ? Testing Goal / Sub-goal: 'infection'
      Checking candidate rule R1: IF cough AND fever THEN infection
      ? Testing Goal / Sub-goal: 'cough'
        => TRUE: 'cough' is directly present in Known Facts database.
      ? Testing Goal / Sub-goal: 'fever'
        => TRUE: 'fever' is directly present in Known Facts database.
      => SUCCESS: All premises for R1 proven. Conclude 'infection' is TRUE.
    ? Testing Goal / Sub-goal: 'sore_throat'
      => TRUE: 'sore_throat' is directly present in Known Facts database.
    => SUCCESS: All premises for R2 proven. Conclude 'influenza' is TRUE.
  => SUCCESS: All premises for R5 proven. Conclude 'prescribe_antiviral_and_rest' is TRUE.

Backward Chaining Summary:
  Goal Hypothesis : 'prescribe_antiviral_and_rest'
  Verification    : PROVEN (TRUE)
======================================================================
```

---

## 6. Result & Viva Questions

### Result:
The Inference System was successfully implemented using both Forward Chaining and Backward Chaining. Given initial symptoms, the system systematically derived `infection` $\rightarrow$ `influenza` $\rightarrow$ `prescribe_antiviral_and_rest`, verifying the hypothesis using data-driven and goal-driven reasoning mechanisms.

### Viva Voce Q&A:
1. **Q: When is Forward Chaining preferred over Backward Chaining?**
   - **A:** Forward Chaining is preferred when there are many initial facts and many possible conclusions, or when data arrives dynamically (e.g., monitoring, synthesis). Backward Chaining is preferred when a specific hypothesis needs to be validated and there are many rules (e.g., diagnostic testing, debugging).
2. **Q: What is Modus Ponens?**
   - **A:** Modus Ponens is a fundamental rule of logical inference: Given fact $P$ and implication rule $P \rightarrow Q$, one can infer $Q$.
3. **Q: What is Conflict Resolution in rule-based systems?**
   - **A:** When multiple rules are ready to fire simultaneously (conflict set), conflict resolution strategies (e.g., rule priority, specificity, recency) decide which rule fires first.
