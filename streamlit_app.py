import streamlit as st

# Set up page title
st.set_page_title("Gym Progress & Weight Adjuster", page_icon="💪")
st.title("🏋️‍♂️ Your 5-Day Gym Companion")
st.subheader("Lose 10-12 kg Goal • 20 Min Cardio + Weight Training")

# Initialize session state to remember weights and progress
if 'weights' not in st.session_state:
    st.session_state.weights = {
        "Bench Press": 20, "Incline Dumbbell Fly": 10, "Tricep Pushdown": 15,
        "Lat Pulldown": 30, "Seated Cable Row": 25, "Bicep Curl": 8,
        "Squat": 30, "Leg Press": 60, "Calf Raise": 20,
        "Overhead Press": 15, "Lateral Raise": 5, "Face Pull": 10
    }

# 5-Day Workout Routine Definition
workouts = {
    "Day 1: Chest & Triceps": ["Bench Press", "Incline Dumbbell Fly", "Tricep Pushdown"],
    "Day 2: Back & Biceps": ["Lat Pulldown", "Seated Cable Row", "Bicep Curl"],
    "Day 3: Active Rest / Cardio Only": [],
    "Day 4: Legs & Abs": ["Squat", "Leg Press", "Calf Raise"],
    "Day 5: Shoulders & Arms": ["Overhead Press", "Lateral Raise", "Face Pull"],
    "Day 6: Active Rest / Cardio Only": [],
    "Day 7: Full Body Flush": ["Bench Press", "Lat Pulldown", "Squat"]
}

# Day Selector
day = st.selectbox("Select Today's Workout Day:", list(workouts.keys()))

# --- CARDIO SECTION ---
st.header("🏃‍♂️ Step 1: Warm-up & Cardio")
st.info("Complete **15–20 minutes** on the Treadmill, Elliptical, or Stairmaster. Aim for a moderate intensity where you can talk but not sing.")
cardio_done = st.checkbox("Mark Cardio as Completed")

# --- WEIGHT TRAINING SECTION ---
st.header("🏋️‍♀️ Step 2: Weight Training (3 Sets x 10-12 Reps)")

exercises = workouts[day]

if not exercises:
    st.success("It's a Rest/Cardio day! Focus on recovery, stretching, and hitting your step goals.")
else:
    for exercise in exercises:
        current_weight = st.session_state.weights[exercise]
        st.write(f"### **{exercise}**")
        st.write(f"Target: 3 Sets of 10-12 reps @ **{current_weight} kg**")
        
        # Feedback buttons for weight adjustment
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(f"Too Easy 🟢", key=f"easy_{exercise}"):
                st.session_state.weights[exercise] += 2.5
                st.experimental_rerun()
                
        with col2:
            st.button("Just Right 🔵", key=f"right_{exercise}")
            
        with col3:
            if st.button(f"Too Difficult 🔴", key=f"hard_{exercise}"):
                st.session_state.weights[exercise] = max(0, st.session_state.weights[exercise] - 2.5)
                st.experimental_rerun()
        
        st.markdown("---")

# --- PROGRESS FOOTER ---
st.sidebar.header("📋 Current Weight Settings")
for ex, wt in st.session_state.weights.items():
    st.sidebar.text(f"{ex}: {wt} kg")
