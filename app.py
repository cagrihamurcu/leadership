
import streamlit as st

st.set_page_config(
    page_title="Tourism Leadership Challenge",
    page_icon="🧭",
    layout="centered"
)

QUESTIONS = [
    {
        "week": "Week 4",
        "topic": "Trait Approach",
        "title": "Confidence or Overconfidence?",
        "scenario": (
            "A hotel manager is highly confident. Employees warn that a new reservation "
            "system has serious problems. The manager says: "
            "\"I know this industry. We will use it anyway.\""
        ),
        "options": [
            "The manager shows ideal self-confidence.",
            "Confidence is becoming overconfidence.",
            "The manager should avoid making any decision.",
            "The problem is only technical, not related to leadership."
        ],
        "answer": 1,
        "explanation": (
            "Confidence can support decision-making, but when it prevents listening, "
            "learning, or reconsidering evidence, it becomes overconfidence."
        ),
        "concept": "Trait Approach"
    },
    {
        "week": "Week 4",
        "topic": "Behavioral Approach",
        "title": "A New Reception Employee",
        "scenario": (
            "A new reception employee has never used the reservation system, makes "
            "frequent mistakes, is nervous, and wants to learn."
        ),
        "options": [
            "Use only people-oriented behavior.",
            "Use only task-oriented behavior.",
            "Combine task-oriented and people-oriented behavior.",
            "Give the employee complete autonomy immediately."
        ],
        "answer": 2,
        "explanation": (
            "The employee needs task clarity and structured guidance, but also support, "
            "constructive feedback, and encouragement."
        ),
        "concept": "Initiating Structure + Consideration"
    },
    {
        "week": "Week 4",
        "topic": "Path–Goal Theory",
        "title": "Which Leadership Behavior?",
        "scenario": (
            "A new tour guide does not know the route and is unsure about the sequence "
            "of activities during the tour."
        ),
        "options": [
            "Directive behavior",
            "Participative behavior",
            "Achievement-oriented behavior",
            "Complete delegation"
        ],
        "answer": 0,
        "explanation": (
            "Directive behavior is appropriate when the follower needs clearer instructions, "
            "standards, or task guidance."
        ),
        "concept": "Path–Goal Theory"
    },
    {
        "week": "Week 4",
        "topic": "Leader–Member Exchange",
        "title": "Trust or Favoritism?",
        "scenario": (
            "A manager gives important information, development opportunities, and flexible "
            "schedules only to two favorite employees."
        ),
        "options": [
            "This always improves team performance.",
            "This is a good example of equal treatment.",
            "This may create perceptions of favoritism and unfairness.",
            "This is transformational leadership."
        ],
        "answer": 2,
        "explanation": (
            "High-quality leader–member relationships can be beneficial, but unequal access "
            "to trust, information, and opportunities may create perceptions of unfairness."
        ),
        "concept": "Leader–Member Exchange (LMX)"
    },
    {
        "week": "Week 4",
        "topic": "Transactional Leadership",
        "title": "Performance and Reward",
        "scenario": (
            "A hotel sales manager says: "
            "\"If customer satisfaction exceeds 90%, the team will receive a bonus.\""
        ),
        "options": [
            "Transactional leadership",
            "Transformational leadership",
            "Laissez-faire leadership",
            "Trait leadership"
        ],
        "answer": 0,
        "explanation": (
            "The statement links a specific performance outcome with a reward. "
            "This reflects transactional leadership."
        ),
        "concept": "Transactional Leadership"
    },
    {
        "week": "Week 4",
        "topic": "Transformational Leadership",
        "title": "Creating Meaning",
        "scenario": (
            "A founder tells the team: "
            "\"We want visitors to experience Ankara, not simply visit it. "
            "Let's redesign every part of the guest journey around authentic local hospitality.\""
        ),
        "options": [
            "Purely transactional leadership",
            "Transformational leadership",
            "Only task-oriented leadership",
            "No leadership behavior is present"
        ],
        "answer": 1,
        "explanation": (
            "The founder is creating a vision, meaning, and commitment to change—key elements "
            "of transformational leadership."
        ),
        "concept": "Transformational Leadership"
    },
    {
        "week": "Week 5",
        "topic": "Expectancy Theory",
        "title": "Why Does the Bonus Fail?",
        "scenario": (
            "A hotel offers a valuable bonus to the best employee, but staff believe "
            "managers choose favorites regardless of actual performance."
        ),
        "options": [
            "Valence is weak.",
            "Instrumentality is weak.",
            "Expectancy is always zero.",
            "The reward is too intrinsic."
        ],
        "answer": 1,
        "explanation": (
            "Employees do not believe that strong performance will reliably lead to the reward. "
            "That means instrumentality is weak."
        ),
        "concept": "Expectancy Theory"
    },
    {
        "week": "Week 5",
        "topic": "Self-Determination Theory",
        "title": "What Supports Motivation?",
        "scenario": (
            "A hotel manager gives an experienced employee some discretion in solving guest "
            "problems, provides training, and encourages strong team relationships."
        ),
        "options": [
            "Autonomy, competence, and relatedness",
            "Only financial incentives",
            "Position power and punishment",
            "Role ambiguity and competition"
        ],
        "answer": 0,
        "explanation": (
            "Self-Determination Theory emphasizes autonomy, competence, and relatedness as "
            "important psychological needs."
        ),
        "concept": "Self-Determination Theory"
    },
    {
        "week": "Week 5",
        "topic": "Goal-Setting Theory",
        "title": "Which Goal Is Better?",
        "scenario": "A hotel wants to improve complaint handling. Which goal is better designed?",
        "options": [
            "\"Do your best with complaints.\"",
            "\"Be more customer-oriented.\"",
            "\"Reduce average complaint response time to under 15 minutes this month.\"",
            "\"Avoid all complaints forever.\""
        ],
        "answer": 2,
        "explanation": (
            "The goal is specific and measurable. Effective goals should also be challenging "
            "but realistic and supported by feedback."
        ),
        "concept": "Goal-Setting Theory"
    },
    {
        "week": "Week 5",
        "topic": "Team Building",
        "title": "A Group Is Not Yet a Team",
        "scenario": (
            "Four hotel employees all try to help with everything. Two people repeat the same task, "
            "another task is forgotten, and employees begin blaming each other."
        ),
        "options": [
            "The main problem is low salary.",
            "The main problem is unclear roles and poor coordination.",
            "The team needs less communication.",
            "The hotel needs more advertising."
        ],
        "answer": 1,
        "explanation": (
            "Teams need clear roles, coordination, shared goals, and mutual responsibility. "
            "Here, role clarity and coordination are the immediate problems."
        ),
        "concept": "Team Building"
    },
    {
        "week": "Week 5",
        "topic": "Communication",
        "title": "Handling an Angry Guest",
        "scenario": (
            "A guest says: \"This is unacceptable. I have been waiting for my room for one hour.\""
        ),
        "options": [
            "\"Check-in time is on the website. Please read it.\"",
            "\"Calm down. This happens sometimes.\"",
            "\"I understand the delay is frustrating. Let me check what happened and what we can do now.\"",
            "\"This is not my responsibility.\""
        ],
        "answer": 2,
        "explanation": (
            "The response acknowledges the concern, avoids defensiveness, checks the situation, "
            "and moves toward a solution. It reflects active listening."
        ),
        "concept": "Active Listening"
    },
    {
        "week": "Week 5",
        "topic": "Negotiation",
        "title": "Position vs. Interest",
        "scenario": (
            "A tour operator says: \"I want a 20% discount.\" "
            "The real reason is that the package must stay within the customer's budget."
        ),
        "options": [
            "The 20% discount is the interest; the budget is the position.",
            "The 20% discount is the position; the budget concern is the interest.",
            "Both are positions.",
            "Both are interests."
        ],
        "answer": 1,
        "explanation": (
            "A position is what a party says it wants. An interest explains why that outcome matters."
        ),
        "concept": "Negotiation: Position vs. Interest"
    },
]

defaults = {
    "started": False,
    "index": 0,
    "score": 0,
    "answered": False,
    "selected": None,
    "answers": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

def restart_game():
    for key, value in defaults.items():
        st.session_state[key] = value

st.title("🧭 Tourism Leadership Challenge")
st.caption("TRZ405 – Tourism Industry Entrepreneurship | Weeks 4–5")

if not st.session_state.started:
    st.subheader("You are the manager of a growing tourism venture.")
    st.write(
        "You will face leadership, motivation, teamwork, communication, and negotiation "
        "problems. Choose the best response and build your leadership score."
    )
    st.info("🎯 12 scenarios • 10 points each • Immediate academic feedback")
    st.markdown(
        """
        **Topics in the game**
        - Leadership traits and behaviors
        - Path–Goal Theory
        - Leader–Member Exchange
        - Transactional and transformational leadership
        - Expectancy Theory
        - Self-Determination Theory
        - Goal-Setting Theory
        - Team building
        - Active listening
        - Negotiation
        """
    )
    if st.button("Start the Challenge", type="primary", use_container_width=True):
        st.session_state.started = True
        st.rerun()

else:
    if st.session_state.index >= len(QUESTIONS):
        max_score = len(QUESTIONS) * 10
        score = st.session_state.score
        percentage = round((score / max_score) * 100)

        st.success("🏁 Challenge Completed!")
        st.metric("Your Score", f"{score} / {max_score}")
        st.progress(percentage / 100)
        st.write(f"**Success rate: {percentage}%**")

        if percentage >= 90:
            st.subheader("🏆 Leadership Strategist")
            st.write("Excellent. You applied the theories consistently across tourism situations.")
        elif percentage >= 75:
            st.subheader("🥇 Strong Tourism Leader")
            st.write("Very good. You understand most core concepts and their applications.")
        elif percentage >= 60:
            st.subheader("🥈 Developing Leader")
            st.write("Good foundation. Review the concepts behind the questions you missed.")
        else:
            st.subheader("📚 Leadership Learner")
            st.write("Review the theories and try the challenge again.")

        with st.expander("Review Your Answers"):
            for i, item in enumerate(st.session_state.answers, start=1):
                icon = "✅" if item["correct"] else "❌"
                st.markdown(
                    f"**{icon} {i}. {item['concept']}**  \n"
                    f"Your answer: {item['selected']}  \n"
                    f"Correct answer: {item['correct_answer']}"
                )

        if st.button("Play Again", use_container_width=True):
            restart_game()
            st.rerun()

    else:
        q = QUESTIONS[st.session_state.index]
        current = st.session_state.index + 1
        total = len(QUESTIONS)

        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"### Scenario {current} of {total}")
            st.caption(f"{q['week']} • {q['topic']}")
        with col2:
            st.metric("Score", st.session_state.score)

        st.progress((current - 1) / total)
        st.subheader(q["title"])
        st.write(q["scenario"])

        option = st.radio(
            "Choose the best answer:",
            q["options"],
            index=None,
            disabled=st.session_state.answered,
            key=f"q_{st.session_state.index}"
        )

        if not st.session_state.answered:
            if st.button("Check Answer", type="primary", use_container_width=True):
                if option is None:
                    st.warning("Please choose an answer first.")
                else:
                    st.session_state.selected = option
                    st.session_state.answered = True
                    selected_index = q["options"].index(option)
                    is_correct = selected_index == q["answer"]

                    if is_correct:
                        st.session_state.score += 10

                    st.session_state.answers.append(
                        {
                            "concept": q["concept"],
                            "selected": option,
                            "correct_answer": q["options"][q["answer"]],
                            "correct": is_correct
                        }
                    )
                    st.rerun()

        else:
            selected_index = q["options"].index(st.session_state.selected)
            is_correct = selected_index == q["answer"]

            if is_correct:
                st.success("✅ Correct! +10 points")
            else:
                st.error("❌ Not quite.")
                st.write(f"**Correct answer:** {q['options'][q['answer']]}")

            st.info(f"**Why?** {q['explanation']}")
            st.caption(f"Academic concept: {q['concept']}")

            button_text = "See Final Score" if current == total else "Next Scenario"
            if st.button(button_text, type="primary", use_container_width=True):
                st.session_state.index += 1
                st.session_state.answered = False
                st.session_state.selected = None
                st.rerun()

        st.divider()
        with st.expander("How scoring works"):
            st.write(
                "Each correct answer gives **10 points**. "
                f"The maximum score is **{len(QUESTIONS) * 10} points**."
            )
