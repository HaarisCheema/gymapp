import streamlit as st

# Setup page layout natively
st.set_page_config(
    page_title="HypeFit • Your 5-Day Gym Companion", 
    page_icon="⚡", 
    layout="centered"
)

# App Titles using standard markdown
st.title("⚡ HypeFit")
st.subheader("Goal: Lose 10-12 kg • 5-Day Dynamic Split")

# Initialize session state to remember weights across weeks
if 'weights' not in st.session_state:
    st.session_state.weights = {
        "Bench Press": 20.0, "Incline Dumbbell Fly": 10.0, "Tricep Pushdown": 15.0,
        "Incline Dumbbell Press": 14.0, "Overhead Tricep Extension": 12.5,
        "Lat Pulldown": 30.0, "Seated Cable Row": 25.0, "Bicep Curl": 8.0,
        "Bent Over Row": 30.0, "Hammer Curl": 8.0,
        "Squat": 30.0, "Leg Press": 60.0, "Calf Raise": 20.0,
        "Bulgarian Split Squat": 10.0, "Leg Curl": 25.0,
        "Overhead Press": 15.0, "Lateral Raise": 5.0, "Face Pull": 10.0,
        "Dumbbell Shoulder Press": 12.0, "Front Raise": 5.0
    }

# Exercise Instructions Dictionary
instructions = {
    "Bench Press": "Lie flat on a bench. Lower the bar smoothly to your mid-chest, then drive it straight up while keeping your feet planted.",
    "Incline Dumbbell Fly": "Set bench to 30°. Keep a slight bend in your elbows, open your arms wide like a hug, and squeeze your chest at the top.",
    "Tricep Pushdown": "Keep elbows pinned to your ribs. Push the cable bar/rope down smoothly, squeezing your triceps at the bottom.",
    "Lat Pulldown": "Sit tall, lean back slightly. Pull the bar down to your upper chest by driving your elbows down toward your back pockets.",
    "Seated Cable Row": "Keep your spine tall. Pull the handle toward your lower stomach, pulling your shoulder blades tightly together.",
    "Bicep Curl": "Keep elbows locked at your sides. Curl the weight up smoothly without swinging your upper body.",
    "Squat": "Keep your chest up and feet shoulder-width apart. Sit back into your hips like sitting in a chair, pushing knees outward.",
    "Leg Press": "Place feet hip-width on the platform. Lower it slowly until your knees are at 90°, then press up (do not lock your knees).",
    "Calf Raise": "Stand on an edge. Drop your heels low for a deep stretch, then explode up onto your tiptoes and hold for 1 second."
}

# --- VISUAL IMAGES / GIFS DICTIONARY ---
# You can replace these URLs with any open-source exercise GIFs or images you find online!
visuals = {
    "Bench Press": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzEwYTM4Y2Y4bW90Y2N4N3R5M2M0bW90Y2N4N3R5M2M0bW90Y2N4/3o7qE0gYsgDCI0SLR6/giphy.gif",
    "Incline Dumbbell Fly": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWRhM2I0M2U0bW90Y2N4N3R5M2M0bW90Y2N4N3R5M2M0bW90Y2N4/l0HlU7e8I5fW6pZ0A/giphy.gif",
    "Squat": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2g0bW90Y2N4N3R5M2M0bW90Y2N4N3R5M2M0bW90Y2N4N3R5M2M0bW90Y2N4/3o7qE4uMcuM9OJT0A0/giphy.gif"
}

# --- THE 5-DAY ROTATING SPLIT ---
week_a = {
    "Day 1: Chest & Triceps (Push A)": ["Bench Press", "Incline Dumbbell Fly", "Tricep Pushdown"],
    "Day 2: Back & Biceps (Pull A)": ["Lat Pulldown", "Seated Cable Row", "Bicep Curl"],
    "Day 3: Legs & Abs (Lower A)": ["Squat", "Leg Press", "Calf Raise"],
    "Day 4: Shoulders & Arms": ["Overhead Press", "Lateral Raise", "Face Pull"],
    "Day 5: Full Body Flush": ["Bench Press", "Lat Pulldown", "Squat"]
}

week_b = {
    "Day 1: Chest & Triceps (Push B)": ["Incline Dumbbell Press", "Bench Press", "Overhead Tricep Extension"],
    "Day 2: Back & Biceps (Pull B)": ["Bent Over Row", "Lat Pulldown", "Hammer Curl"],
    "Day 3: Legs & Abs (Lower B)": ["Bulgarian Split Squat", "Leg Curl", "Calf Raise"],
    "Day 4: Shoulders & Upper Body": ["Dumbbell Shoulder Press", "Lateral Raise", "Front Raise"],
    "Day 5: Full Body Challenge": ["Incline Dumbbell Press", "Seated Cable Row", "Leg Press"]
}

# Week & Day Selectors
col_wk, col_day = st.columns(2)
with col_wk:
    current_week = st.radio("🗓️ Select Current Week:", ["Week A", "Week B"])

current_routine = week_a if current_week == "Week A" else week_b

with col_day:
    day = st.selectbox("📆 Select Gym Day:", list(current_routine.keys()))

st.divider()

# --- CARDIO SECTION ---
st.markdown("### 🏃‍♂️ Step 1: Metabolic Warm-up & Cardio")
st.info("**Target:** 15–20 minutes on the Treadmill, Stairmaster, or Bike. Keep a brisk pace!")
cardio_done = st.checkbox("Cardio Completed", key="cardio_chk")

st.divider()

# --- WEIGHT TRAINING SECTION ---
st.markdown("### 🏋️‍♀️ Step 2: Main Lifting Session")

exercises = current_routine[day]

for exercise in exercises:
    current_weight = st.session_state.weights[exercise]
    
    st.markdown(f"#### {exercise}")
    st.caption(f"💡 {instructions.get(exercise, '')}")
    
    # NEW: Displays visual media if a URL exists in our dictionary
    if exercise in visuals:
        st.image(visuals[exercise], width=350)
        
    st.write(f"**Target:** 3 Sets × 10-12 reps @ **{current_weight} kg**")
    
    # Custom feedback buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button(f"Too Easy 🟢", key=f"easy_{exercise}_{current_week}"):
            st.session_state.weights[exercise] += 2.5
            st.rerun()
            
    with col2:
        st.button("Just Right 🔵", key=f"right_{exercise}_{current_week}")
        
    with col3:
        if st.button(f"Too Hard 🔴", key=f"hard_{exercise}_{current_week}"):
            st.session_state.weights[exercise] = max(0.0, st.session_state.weights[exercise] - 2.5)
            st.rerun()
    
    st.divider()

# --- SIDEBAR TRACKER ---
st.sidebar.header("📋 Weight Tracker Matrix")
for ex, wt in st.session_state.weights.items():
    if ex in exercises:
        st.sidebar.markdown(f"**{ex}:** `{wt} kg` 🔥")
    else:
        st.sidebar.text(f"{ex}: {wt} kg")
