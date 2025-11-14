# coded by Nidafatima R Shaikh 
#use dark theme for visuals


import streamlit as st
import matplotlib.pyplot as plt
import time 
from datetime import date


# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = "student"

# Page configuration and styling
st.set_page_config(page_title="Login | Student Success Dashboard", layout="centered")
st.markdown("""
    <style>
    div[data-testid="stAppViewContainer"] {
        padding: 20px;
        font-size: 22px;
        background-color: black;
        color: white;
    }
    body {
        font-family: 'Segoe UI', sans-serif;
        font-size: 22px;
        background-color: black;
        color: white;
    }
    input {
        border-radius: 6px;
        padding: 12px;
        font-size: 20px;
        border: 1px solid #ccc;
        background-color: #222;
        color: white;
    }
    .stButton button {
        background-color: #003366;
        color: white;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 20px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Login screen
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align:center;'>🚀 Welcome to the Student Success Dashboard</h2>", unsafe_allow_html=True)
    st.write("Log in to unlock insights, trends, and performance metrics that matter.")
    email = st.text_input("📧 Enter your email to begin your journey", placeholder="name@example.com  in case of professor use 'professor' in place of name")
    password = st.text_input("🔒 Your secret key (password)", type="password", placeholder="name123 and same for professor as above instructions")

    if st.button("Login"):
        if email.endswith("example.com"):
            username = email.split("@")[0]
            expected_password = f"{username}123"
            if password == expected_password:
                st.session_state.logged_in = True
                st.session_state.role = "professor" if username == "professor" else "student"
                st.rerun()
                
                st.success(f"🎉 Welcome {username.capitalize()}! Your personalized dashboard awaits.")
            else:
                st.error("❌ Invalid password. Please try again.")
        else:
            st.error("❌ Invalid email. Please try again.")

# Dashboard after login
else:
    # Student dashboard
    if st.session_state.role == "student":
        st.markdown("---")
        st.title("🎓 Student Success Dashboard")

        st.sidebar.title("📌 Navigation")
        page = st.sidebar.radio("Choose a section", [
            "Overview", "Progress", "Study Mode", "Quiz","Timetable", "Resources", "Help Center", "Feedback"
        ])
        if page=="Overview":
            if "overview_data" not in st.session_state:
                st.session_state.overview_data = {
            "modules_total": 15,
        "modules_completed": 12,
        "time_spent": 8,
        "avg_grade": 88,
        "reflection": ""
            }

        


            if "mood" not in st.session_state:
                st.session_state.mood = None


            st.subheader("📊 Overview")
            st.write("Welcome to your academic snapshot. Here's how you're doing overall.")

            completed = st.session_state.overview_data["modules_completed"]
            total = st.session_state.overview_data["modules_total"]
            time_spent = st.session_state.overview_data["time_spent"]
            avg_grade = st.session_state.overview_data["avg_grade"]

            col1, col2, col3 = st.columns(3)
            col1.metric("Modules", f"{completed} / {total}")
            col2.metric("Time Spent", f"{time_spent} hrs / week")
            col3.metric("Avg Grade", f"{avg_grade} / 100 %")

            st.session_state.overview_data["modules_completed"] = col1.number_input(
    "Modules Completed", min_value=0,
    max_value=st.session_state.overview_data["modules_total"],
    value=st.session_state.overview_data["modules_completed"]
)
            st.session_state.overview_data["time_spent"] = col2.number_input(
    "Time Spent (hrs this week)", min_value=0,
    value=st.session_state.overview_data["time_spent"]
)
            st.session_state.overview_data["avg_grade"] = col3.number_input(
    "Average Grade (%)", min_value=0, max_value=100,
    value=st.session_state.overview_data["avg_grade"]
)
            completed = st.session_state.overview_data["modules_completed"]
            total = st.session_state.overview_data["modules_total"]
            pending = total - completed

            labels = ['Completed', 'Pending']
            size = [completed, pending]
            colors = ['#66b3ff', '#ff9999']
            fig, ax = plt.subplots(figsize=(2.75, 1.75))
            fig.patch.set_alpha(0.0)
            ax.pie(size, colors=colors, labels=labels, startangle=90, autopct="%1.1f%%")
            ax.axis('equal')
            st.pyplot(fig)





            st.write("📝 **Reflection:** What did you learn this week?")
            st.session_state.overview_data["reflection"] = st.text_area(
    "What did you learn this week?",
    value=st.session_state.overview_data["reflection"],
    placeholder="Your thoughts..."
)  
            mood = st.radio("How are you feeling today?", ["😊 Great", "😐 Okay", "😟 Stressed"])
            st.session_state.mood = mood

            if mood == "😊 Great":
                st.success("That's awesome! Keep riding that wave of motivation. 🌟")
            elif mood == "😐 Okay":
                st.info("You're doing fine. A small step today is still progress. 💪")
            elif mood == "😟 Stressed":
                st.warning("Take a breath. You're not alone, and it's okay to pause. 🌱")

            st.markdown("### ⚙️ Manage Modules")
            new_total = st.number_input("Set Total Modules", min_value=1,
    value=st.session_state.overview_data["modules_total"]
)
            st.session_state.overview_data["modules_total"] = new_total

            if st.button("🔄 Reset Overview"):
                st.session_state.overview_data = {
        "modules_total": 15,
        "modules_completed": 0,
        "time_spent": 0,
        "avg_grade": 0,
        "reflection": ""
    }
            st.success("Overview reset successfully.")

        elif page== "Progress":
            if "progress_data" not in st.session_state:
                st.session_state.progress_data = {
        "total_modules": 15,
        "completed_modules": 12,
        "weekly_progress": [2, 4, 7, 10, 12],
        "reflection_good": "",
        "reflection_improve": "",
        "goal_next_week": "",
        "mood_progress": "😐 Neutral"
    }

            st.subheader("📈 Progress Tracker")
            st.write("Here's a snapshot of your academic journey so far.")

            col1, col2, col3 = st.columns(3)
            st.session_state.progress_data["total_modules"] = col1.number_input(
    "Total Modules", min_value=1, value=st.session_state.progress_data["total_modules"], key="total_modules_input"
)
            st.session_state.progress_data["completed_modules"] = col2.number_input(
    "Completed Modules", min_value=0, max_value=st.session_state.progress_data["total_modules"],
    value=st.session_state.progress_data["completed_modules"], key="completed_modules_input"
)
            remaining = st.session_state.progress_data["total_modules"] - st.session_state.progress_data["completed_modules"]
            col3.metric("Remaining", f"{remaining}")

            st.progress(st.session_state.progress_data["completed_modules"] / st.session_state.progress_data["total_modules"])

            st.markdown("### 📊 Module Completion Over Time")
            if st.session_state.progress_data["weekly_progress"]:
                weeks = [f"Week {i+1}" for i in range(len(st.session_state.progress_data["weekly_progress"]))]
                fig, ax = plt.subplots()
                ax.plot(weeks, st.session_state.progress_data["weekly_progress"], marker='o', color='#66b3ff')
                ax.set_facecolor("#111")
                fig.patch.set_facecolor("#111")
                ax.set_title("Modules Completed Over Time", fontsize=14, color="white")
                ax.set_xlabel("Weeks", color="white")
                ax.set_ylabel("Modules", color="white")
                ax.tick_params(colors="white")
                ax.grid(True, color="#444")
                st.pyplot(fig)
            new_week_modules = st.number_input("Modules completed this week", min_value=0, key="new_week_input")
            st.session_state.new_week_modules = new_week_modules

            if not st.session_state.progress_data["weekly_progress"]:
                st.info("No weekly progress data yet. Add a week to begin tracking 📈")

            if st.button("➕ Add Week"):
                st.session_state.progress_data["weekly_progress"].append(st.session_state.new_week_modules)
                st.session_state.new_week_modules = 0
                st.rerun()

                 
            st.markdown("### 📝 Weekly Reflection")
            st.session_state.progress_data["reflection_good"] = st.text_area(
            "What went well?",
    value=st.session_state.progress_data["reflection_good"],
    placeholder="Write about your wins, breakthroughs, or habits that helped."
)
            st.session_state.progress_data["reflection_improve"] = st.text_area(
    "What could improve?",
    value=st.session_state.progress_data["reflection_improve"],
    placeholder="Mention any blockers, distractions, or areas to focus on."
)
            st.session_state.progress_data["goal_next_week"] = st.text_area(
    "Next week's goal:",
    value=st.session_state.progress_data["goal_next_week"],
    placeholder="Set a clear, achievable goal for the coming week."
)

            st.markdown("### 🌈 Mood Check-In")
            mood = st.radio(
    "How do you feel about your progress?",
    ["🚀 Proud", "😐 Neutral", "😟 Concerned"],
    index=["🚀 Proud", "😐 Neutral", "😟 Concerned"].index(st.session_state.progress_data["mood_progress"])
)
            st.session_state.progress_data["mood_progress"] = mood

            if mood == "🚀 Proud":
                st.success("Amazing! Keep up the momentum. You're building something great.")
            elif mood == "😐 Neutral":
                st.info("You're steady. A small push can turn this into a breakthrough week.")
            elif mood == "😟 Concerned":
                st.warning("It's okay to feel stuck. Let’s reset and take one step forward.")

            if st.button("🔄 Reset Progress"):
                st.session_state.progress_data = {
        "total_modules": 15,
        "completed_modules": 0,
        "weekly_progress": [],
        "reflection_good": "",
        "reflection_improve": "",
        "goal_next_week": "",
        "mood_progress": "😐 Neutral"
    }
                st.success("Progress reset successfully.")
                st.rerun()      

        elif page == "Feedback":
            st.subheader("📝 Feedback & Notes")
            st.write("Share your thoughts about System A — what worked, what didn’t, and what could improve.")

    
            if "system_a_feedback" not in st.session_state:
                st.session_state.system_a_feedback = ""
            if "system_a_rating" not in st.session_state:
                st.session_state.system_a_rating = "⭐️⭐️⭐️"
            if "system_a_mood" not in st.session_state:
                st.session_state.system_a_mood = "🧠 Thoughtful"

            st.markdown("### 💬 Your Feedback on this dashboard")
            st.session_state.system_a_feedback = st.text_area(
        "What did you think of this dasboard?",
        value=st.session_state.system_a_feedback,
        placeholder="Was it helpful? Confusing? Share your experience.",
        height=200
         )

    
            st.markdown("### 📊 Rate this dashboard")
            st.session_state.system_a_rating = st.selectbox(
        "Choose a rating:",
        ["⭐️", "⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️"],
        index=["⭐️", "⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️"].index(st.session_state.system_a_rating)
    )

            st.markdown("### 🎭 Tag the tone of your feedback")
            st.session_state.system_a_mood = st.selectbox(
        "How would you describe your feedback?",
        ["🧠 Thoughtful", "🎯 Focused", "😕 Confused", "💡 Inspired", "😤 Frustrated"],
        index=["🧠 Thoughtful", "🎯 Focused", "😕 Confused", "💡 Inspired", "😤 Frustrated"].index(st.session_state.system_a_mood)
    )

            st.markdown("### 📌 Summary")
            st.write(f"**Rating:** {st.session_state.system_a_rating}")
            st.write(f"**Tone:** {st.session_state.system_a_mood}")
            st.write("**Feedback:**")
            st.markdown(
        f"> {st.session_state.system_a_feedback}"
        if st.session_state.system_a_feedback
        else "_No feedback submitted yet._"
        )

        elif page == "Study Mode":
            st.subheader("🌿 Personal Space")
            st.write("A quiet corner to focus your mind and flow.")



            st.markdown("### ⏱️ Focus Mode")
            st.session_state.pomodoro_mode = st.checkbox("Enable Pomodoro Mode")
            if "pomodoro_mode" not in st.session_state:
                st.session_state.pomodoro_mode = False
            if "pomodoro_state" not in st.session_state:
                st.session_state.pomodoro_state = "Focus"
            if "pomodoro_minutes" not in st.session_state:
                st.session_state.pomodoro_minutes = 25
            if "pomodoro_running" not in st.session_state:
                st.session_state.pomodoro_running = False
            

            if st.session_state.pomodoro_mode:
                st.markdown("### ⏳ Pomodoro Timer")
                st.write(f"**Mode:** {st.session_state.pomodoro_state}")
                st.write(f"**Time Remaining:** {st.session_state.pomodoro_minutes} minutes")
                if not st.session_state.pomodoro_running:
                    if st.button("▶️ Start Timer"):
                        st.session_state.pomodoro_running = True
                        st.toast("Pomodoro started!")
                        if st.session_state.pomodoro_running:
                            with st.empty():
                                for i in range(st.session_state.pomodoro_minutes, 0, -1):
                                    st.write(f"⏳ {i} minutes remaining...")
                                    time.sleep(1)

                                st.session_state.pomodoro_running = False

                                if st.session_state.pomodoro_state == "Focus":
                                    st.session_state.pomodoro_state = "Break"
                                    st.session_state.pomodoro_minutes = 5
                                    st.success("✅ Focus session complete! Time for a 5-minute break.")
                                else:
                                    st.session_state.pomodoro_state = "Focus"
                                    st.session_state.pomodoro_minutes = 25
                                    st.info("🔁 Break over! Ready to focus again.")

        elif page == "Timetable":
            st.subheader("📅 Flexible Timetable Maker")
            st.write("Plan your week with subjects, notes, and assignment deadlines — no fixed time slots.")

            
            SUBJECTS = [
                "Data Structures", "Algorithms", "Operating Systems", "Computer Networks",
                "Database Management Systems", "Software Engineering", "Python Programming", "Web Development"
            ]

        

            DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            if "daywise_timetable" not in st.session_state:
                st.session_state.daywise_timetable = {day: [] for day in DAYS}
            if "daywise_notes" not in st.session_state:
                st.session_state.daywise_notes = {day: "" for day in DAYS}
            if "daywise_deadlines" not in st.session_state:
                st.session_state.daywise_deadlines = {day: {} for day in DAYS}
            for day in DAYS:
                st.markdown(f"<h3 style='margin-bottom:0.2em'>{day}</h3>", unsafe_allow_html=True)
                selected_subjects=st.multiselect(
                f"Select subjects for {day}:",SUBJECTS,default=st.session_state.daywise_timetable[day],key=f"{day}_subjects"
            )
                st.session_state.daywise_timetable[day]=selected_subjects
                note = st.text_area(
                f"Notes for {day}:",
                value=st.session_state.daywise_notes[day],
                key=f"{day}_note")
                st.session_state.daywise_notes[day]=note
                st.markdown("📅 Assignment Deadlines")
                for subject in selected_subjects:
                    deadline = st.date_input(
                f"Deadline for {subject} on {day}:",
                key=f"{day}_{subject}_deadline")
                    st.session_state.daywise_deadlines[day][subject] = deadline
            st.markdown("## 🧠 Weekly Overview")
            for day in DAYS:
               st.markdown(f"### {day}")
               st.write("Subjects:", ", ".join(st.session_state.daywise_timetable[day]))
               st.write("Notes:", st.session_state.daywise_notes[day])
               for subject, deadline in st.session_state.daywise_deadlines[day].items():
                    st.write(f"{subject}: {deadline.strftime('%A, %d %B %Y')}")
               st.markdown("---")
            st.markdown("🪞 Reflect on your week below or add final thoughts:")
            reflection = st.text_area("Your reflections:", key="weekly_reflection")

        elif page == "Resources":
            st.subheader("💻 Resources for CSE Students")
            st.write("Explore curated books, platforms, and tools to support your coding journey.")

            st.markdown("### 📚 Recommended Books")
            st.markdown("- [Cracking the Coding Interview](https://www.amazon.in/dp/0984782850)")
            st.markdown("- [Introduction to Algorithms – Cormen](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)")
            st.markdown("- [Data Structures and Algorithms Made Easy – Karumanchi](https://www.amazon.in/dp/819324527X)")
            st.markdown("- [Competitive Programming – Halim](https://www.amazon.in/dp/153286078X)")
            st.markdown("- [Elements of Programming Interviews](https://www.amazon.in/dp/1479274836)")

            st.markdown("### 💻 Coding Platforms")
            st.markdown("- [GeeksforGeeks](https://www.geeksforgeeks.org/)")
            st.markdown("- [LeetCode](https://leetcode.com/)")
            st.markdown("- [HackerRank](https://www.hackerrank.com/)")
            st.markdown("- [Codeforces](https://codeforces.com/)")
            st.markdown("- [CodeChef](https://www.codechef.com/)")
            st.markdown("- [Exercism](https://exercism.org/)")

            st.markdown("### 📝 Personal Notes")
            if "resource_notes" not in st.session_state:
                st.session_state.resource_notes=""
            notes=st.text_area("Personal Notes",value=st.session_state.resource_notes,placeholder="Add your own links, reminders, or reflections here...")
            st.session_state.resource_notes=notes
        elif page == "Help Center":
            st.subheader("🛟 Help Center")
            st.write("Find answers, guidance, and tips to make the most of MindMesh.")

            st.markdown("### ❓ Frequently Asked Questions")

            with st.expander("How do I use the Timetable Maker?"):
                st.write("""
                    Go to the Timetable page, select subjects for each day, add notes, and set deadlines.
                    Your selections are saved automatically and previewed in a weekly overview.
                """)

            with st.expander("How do I track my progress?"):
                st.write("""
                    Visit the Progress page to view your module completion chart, weekly reflections, and mood check-ins.
                    You can also set goals and monitor your academic journey.
                """)

            with st.expander("Can I save personal notes?"):
                st.write("""
                    Yes! In the Resources page, use the Personal Notes section.
                    Your notes are remembered across sessions and can be used for links, reminders, or reflections.
                """)

            with st.expander("What is the Personal Space for?"):
                st.write("""
                    It’s your emotional and focus zone — enable Pomodoro mode, track your focus sessions,
                    and reflect on your mood to stay balanced and motivated.
                """)

            with st.expander("How do quizzes work?"):
                st.write("""
                    Professors upload MCQs, and students can take quizzes with instant scoring.
                    Your submissions are saved and visible to professors for analysis.
                """)

            st.markdown("### 🧭 Getting Started")
            st.info("Start with the Overview page to set your goals and explore each module. MindMesh is designed to grow with you.")

            st.markdown("### 📬 Need More Help?")
            st.write("If you're stuck or have ideas to improve MindMesh, reach out to your mentor or leave feedback in the Feedback page.")
        elif page == "Quiz":
            st.subheader("🧠 Quiz Time: Test Your Knowledge")
            st.write("""
                Welcome to your interactive quiz zone! 🎯  
                Challenge yourself with quick questions, get instant feedback, and learn as you go.  
                Each question has one correct answer — choose wisely and see how you score!
            """)

            if "quiz_data" not in st.session_state:
                st.warning("⚠️ No quiz has been uploaded yet by the professor.")
            else:
                name = st.text_input("Enter your name to begin:")
                if name:
                    score = 0
                    student_answers = []

                    st.markdown("### 📋 Your Quiz")
                    for i, item in enumerate(st.session_state.quiz_data):
                        st.write(f"**Q{i+1}:** {item['question']}")
                        selected = st.radio("Choose your answer:", item["options"], key=f"q_{i}")
                        student_answers.append(selected)
                        if selected.strip().lower() == item["correct"].strip().lower():
                            score += 1

                    if st.button("Submit Quiz"):
                        st.success(f"🎉 {name}, you scored {score} out of {len(st.session_state.quiz_data)}")
                        if "results" not in st.session_state:
                            st.session_state.results = []
                        st.session_state.results.append({
                            "name": name,
                            "score": score,
                            "total": len(st.session_state.quiz_data),
                            "answers": student_answers
                        })

    # Professor dashboard
    elif st.session_state.role == "professor":
        page = st.sidebar.radio("Professor Panel", ["Upload MCQs", "Analyze Answers"])

        if page == "Upload MCQs":
            st.subheader("📤 Upload MCQ Files")
            st.markdown("""
                ### 📄 File Format Instructions

                Please upload three files:

                - **Questions File**: Each line should contain one full MCQ question.
                - **Answers File**: Each line should contain the correct answer for the corresponding question.
                - **Options File**: Each line should contain comma-separated options for each question.

                **Make sure the order of questions and answers matches line by line.**
            """)

            questions_file = st.file_uploader("Upload Questions File (.txt or .csv)", type=["txt", "csv"])
            correct_file = st.file_uploader("Upload Correct Answers File (.txt or .csv)", type=["txt", "csv"])
            options_file = st.file_uploader("Upload Options File (.txt)", type=["txt"])

            if questions_file and correct_file and options_file:
                questions = questions_file.read().decode("utf-8").splitlines()
                correct = correct_file.read().decode("utf-8").splitlines()
                options_raw = options_file.read().decode("utf-8").splitlines()
                options = [line.split(",") for line in options_raw]

                if len(questions) != len(correct):
                    st.error("❌ The number of questions and answers does not match. Please check your files.")
                elif len(questions) == len(correct) == len(options):
                    st.session_state.quiz_data = [
                        {"question": q, "correct": c, "options": o}
                        for q, c, o in zip(questions, correct, options)
                    ]

                    st.markdown("### ✅ Preview of Uploaded MCQs")
                    for i in range(len(questions)):
                        st.write(f"**Q{i+1}:** {questions[i]}")
                        st.write(f"✅ Correct Answer: {correct[i]}")
                        st.markdown("---")

                    if st.button("Publish Quiz"):
                        st.success("✅ Quiz published successfully and is now available to students.")

        elif page == "Analyze Answers":
            st.subheader("📊 Student Submissions")
            if "results" in st.session_state:
                for entry in st.session_state.results:
                    st.write(f"👤 {entry['name']} — Score: {entry['score']} / {entry['total']}")
                    for i, ans in enumerate(entry["answers"]):
                        st.write(f"Q{i+1}: {ans}")
                    st.markdown("---")
            else:
                st.info("No student submissions yet.")
with st.sidebar:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
st.markdown("""<hr style='margin-top:2em; margin-bottom:0.5em; border:1px solid #444;'>""", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:#888;'>Crafted with clarity and care by Nidafatima R Shaikh</p>", unsafe_allow_html=True)




































