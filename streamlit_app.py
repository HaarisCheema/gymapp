import streamlit as st

# Custom page config with a dark/modern vibe layout
st.set_page_config(
    page_title="HypeFit • Your 5-Day Gym Companion", 
    page_icon="⚡", 
    layout="centered"
)

# Custom CSS for modern styling and clean typography
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    h1 { color: #FF4B4B; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 800; }
    h3 { color: #FAFAFA; font-weight: 600; margin-top: 20px; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .instruction-text { color: #A3A8B4; font-size: 14px; font-style: italic; margin-bottom: 15px; }
</style>
""", unsafe_allowed_html=True)

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
    "Incline Dumbbell Press": "Set bench to 30°. Press dumbbells straight up over your chest. Lower down until elbows pass your torso.",
    "Tricep Pushdown": "Keep elbows pinned to your ribs. Push the cable bar/rope down smoothly, squeezing your triceps at the bottom.",
    "Overhead Tricep Extension": "Hold a dumbbell or cable behind your head. Keep your elbows facing forward and extend your hands up toward the ceiling.",
    "Lat Pulldown": "Sit tall, lean back slightly. Pull the bar down to your upper chest by driving your elbows down toward your back pockets.",
    "Seated Cable Row": "Keep your spine tall. Pull the handle toward your lower stomach, pulling your shoulder blades tightly together.",
    "Bicep Curl": "Keep elbows locked at your sides. Curl the weight up smoothly without swinging your upper body.",
    "Bent Over Row": "Hinge at your hips, keeping your back completely flat. Pull the barbell up toward your belly button.",
    "Hammer Curl": "Hold dumbbells with palms facing each other (like a hammer). Curl upward to target your forearms and biceps.",
    "Squat": "Keep your chest up and feet shoulder-width apart. Sit back into your hips like sitting in a chair, pushing knees outward.",
    "Leg Press": "Place feet hip-width on the platform. Lower it slowly until your knees are at 90°, then press up (do not lock your knees).",
    "Calf Raise": "Stand on an edge. Drop your heels low for a deep stretch, then explode up onto your tiptoes and hold for 1 second.",
    "Bulgarian Split Squat": "Place one foot behind you on a bench. Drop your back knee toward the floor while keeping your front knee stable.",
    "Leg Curl": "Lie or sit in the machine. Drive your heels down toward your glutes, squeezing your hamstrings hard at the peak.",
    "Overhead Press": "Stand tight, core engaged. Press the barbell from your collarbone straight up over your head until arms lock.",
    "Dumbbell Shoulder Press": "Sit or stand with weights at ear level. Press straight up overhead without letting your lower back arch.",
    "Lateral Raise": "Stand tall, lead with your elbows out to the sides. Bring hands up to shoulder height to build wide, capped shoulders.",
    "Front Raise": "Raise dumbbells directly out in front of you to eye level, controlling the weight smoothly on the way back down.",
    "Face Pull": "Pull the cable rope toward your nose, flaring your elbows high and wide to hit your upper back and rear shoulders."
}

# --- THE 5-DAY ROTATING SPLIT ---
# Week A Setup
week_a = {
    "Day 1: Chest & Triceps (Push A)": ["Bench Press", "Incline Dumbbell Fly", "Tricep Pushdown"],
    "Day 2: Back & Biceps (Pull A)": ["Lat Pulldown", "Seated Cable Row", "Bicep Curl"],
    "Day 3: Legs & Abs (Lower A)": ["Squat", "Leg Press", "Calf Raise"],
    "Day 4: Shoulders & Arms": ["Overhead Press", "Lateral Raise", "Face Pull"],
    "Day 5: Full Body Flush": ["Bench Press", "Lat Pulldown", "Squat"]
}

# Week B Setup (Variation week for muscle confusion)
week_b = {
    "Day 1: Chest & Triceps (Push B)": ["Incline Dumbbell Press", "Bench Press", "Overhead Tricep Extension"],
    "Day 2: Back & Biceps (Pull B)": ["Bent Over Row", "Lat Pulldown", "Hammer Curl"],
    "Day 3: Legs & Abs (Lower B)": ["Bulgarian Split Squat", "Leg Curl", "Calf Raise"],
    "Day 4: Shoulders & Upper Body": ["Dumbbell Shoulder Press", "Lateral Raise", "Front Raise"],
    "Day 5: Full Body Challenge": ["Incline Dumbbell Press", "Seated Cable Row", "Leg Press"]
}

# Week & Day Selectors (Clean layout columns)
col_wk, col_day = st.columns(2)
with col_wk:
    current_week = st.radio("🗓️ Select Current Week:", ["Week A", "Week B"])

current_routine = week_a if current_week == "Week A" else week_b

with col_day:
    day = st.selectbox("📆 Select Gym Day:", list(current_routine.keys()))

st.markdown("---")

# --- CARDIO SECTION ---
st.markdown("### 🏃‍♂️ Step 1: Metabolic Warm-up & Cardio")
st.info("**Target:** 15–20 minutes on the Treadmill, Stairmaster, or Bike. Keep a brisk pace!")
cardio_done = st.checkbox("Cardio Completed", key="cardio_chk")

st.markdown("---")

# --- WEIGHT TRAINING SECTION ---
st.markdown("### 🏋️‍♀️ Step 2: Main Lifting Session")
st.caption("Perform 3 Sets of 10-12 Repetitions per exercise.")

exercises = current_routine[day]

for exercise in exercises:
    current_weight = st.session_state.weights[exercise]
    
    st.markdown(f"#### **{exercise}**")
    # Display the written text instructions dynamically
    st.markdown(f"<div class='instruction-text'>💡 {instructions.get(exercise, '')}</div>", unsafe_allowed_html=True)
    st.write(f"**Target:** 3 Sets × 10-12 reps @ `{current_weight} kg`")
    
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
    
    st.markdown("<br>", unsafe_allowed_html=True)

# --- SIDEBAR TRACKER ---
st.sidebar.header("📋 Weight Tracker Matrix")
st.sidebar.caption("This updates instantly based on your inputs.")
for ex, wt in st.session_state.weights.items():
    if ex in exercises:
        st.sidebar.markdown(f"**{ex}:** `{wt} kg` 🔥")
    else:
        st.sidebar.text(f"{ex}: {wt} kg")
