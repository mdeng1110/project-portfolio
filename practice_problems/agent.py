import random
from collections import defaultdict
import time

class StudyBuddy:
    def __init__(self, topic='multiplication', duration_minutes=10, num_questions=10):
        self.topic = topic
        self.duration_minutes = duration_minutes
        self.num_questions = num_questions
        self.progress = []
        # Track performance per multiplier (2..12)
        self.stats = defaultdict(lambda: {'asked': 0, 'correct': 0})
        # Initial pool of multipliers
        self.pool = list(range(2, 13))
        random.shuffle(self.pool)
        self.start_time = None

    def generate_question(self):
        """Pick a question, biasing toward weak areas."""
        weights = []
        for m in self.pool:
            s = self.stats[m]
            asked = s['asked']
            correct = s['correct']
            acc = (correct / asked) if asked > 0 else 0.5  # assume neutral if no data
            weakness = 1 - acc
            weights.append(weakness + 0.2)  # baseline so all are possible
        multiplier = random.choices(self.pool, weights=weights, k=1)[0]
        multiplicand = random.randint(1, 12)
        question = f"{multiplicand} x {multiplier}"
        answer = multiplicand * multiplier
        return multiplier, question, answer

    def give_hint(self, multiplicand, multiplier):
        """Simple hint: break it down into easier parts."""
        return f"Hint: {multiplicand} x {multiplier} = {multiplicand} x ({multiplier-1}) + {multiplicand}"

    def record_result(self, multiplier, correct):
        self.stats[multiplier]['asked'] += 1
        if correct:
            self.stats[multiplier]['correct'] += 1

    def summarize(self):
        """Show performance and suggest next steps."""
        total = len(self.progress)
        correct = sum(1 for p in self.progress if p['correct'])
        lines = [
            f"Session summary — topic: {self.topic}",
            f"Duration target: {self.duration_minutes} minutes",
            f"Questions asked: {total} | Correct: {correct}"
        ]
        # Performance by multiplier
        perf = []
        for m in sorted(self.stats.keys()):
            s = self.stats[m]
            asked = s['asked']
            if asked == 0:
                continue
            acc = s['correct'] / asked
            perf.append((m, asked, acc))
        if perf:
            lines.append("Performance by multiplier:")
            for m, asked, acc in perf:
                lines.append(f"  {m}: {asked} asked, {acc:.0%} accuracy")
        # Weak spots
        weak = [m for m, asked, acc in perf if asked >= 2 and acc < 0.7]
        if weak:
            lines.append("Weak spots detected: " + ", ".join(map(str, weak)))
            lines.append("Next step: practice these multipliers more!")
        else:
            lines.append("No major weaknesses detected — great job!")
        return "\n".join(lines)

    def run_simulation(self, simulated_answers):
        """Simulate a session with preloaded answers (for demo/testing)."""
        self.start_time = time.time()
        print(f"Starting study session: {self.num_questions} questions\n")
        for i in range(self.num_questions):
            mult, q_text, correct_answer = self.generate_question()
            print(f"Q{i+1}: {q_text} = ?")
            # Use simulated answers if provided
            if i < len(simulated_answers):
                user_ans = simulated_answers[i]
            else:
                # fallback: mostly correct
                user_ans = correct_answer if random.random() < 0.8 else correct_answer + 1
            if user_ans == correct_answer:
                print(f"  Your answer: {user_ans} ✅ Correct!")
                correct_bool = True
            else:
                hint = self.give_hint(int(q_text.split(' x ')[0]), mult)
                print(f"  Your answer: {user_ans} ❌ Wrong. Correct: {correct_answer}. {hint}")
                correct_bool = False
            self.record_result(mult, correct_bool)
            self.progress.append({
                'question': q_text,
                'answer': correct_answer,
                'given': user_ans,
                'correct': correct_bool
            })
            time.sleep(0.1)
        print("\n" + self.summarize())



agent = StudyBuddy(duration_minutes=10, num_questions=10)
for i in range(agent.num_questions):
    mult, q_text, correct_answer = agent.generate_question()
    user_ans = int(input(f"Q{i+1}: {q_text} = "))
    if user_ans == correct_answer:
        print("Correct!")
        agent.record_result(mult, True)
    else:
        print("Wrong. ", agent.give_hint(int(q_text.split(' x ')[0]), mult))
        agent.record_result(mult, False)
print(agent.summarize())
