import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Robotic Arm FK Simulator",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 2D Robotic Arm Forward Kinematics Simulator")

st.write("""
This project simulates a 2-link robotic arm and calculates the real-time position of the end-effector using forward kinematics.
It is useful for understanding robotic arm motion, joint angles, workspace, and coordinate calculation.
""")

# Sidebar inputs
st.sidebar.header("Input Parameters")

L1 = st.sidebar.slider("Link 1 Length", 1.0, 20.0, 10.0)
L2 = st.sidebar.slider("Link 2 Length", 1.0, 20.0, 8.0)

theta1_deg = st.sidebar.slider("Joint 1 Angle θ1 (degrees)", -180, 180, 45)
theta2_deg = st.sidebar.slider("Joint 2 Angle θ2 (degrees)", -180, 180, 30)

# Convert degrees to radians
theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

# Base point
x0, y0 = 0, 0

# Joint 1 position
x1 = L1 * np.cos(theta1)
y1 = L1 * np.sin(theta1)

# End-effector position
x2 = x1 + L2 * np.cos(theta1 + theta2)
y2 = y1 + L2 * np.sin(theta1 + theta2)

# Layout columns
left_col, right_col = st.columns([1, 1.4])

with left_col:
    st.subheader("📌 Calculated Coordinates")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Joint 1 X", round(x1, 2))
        st.metric("End Effector X", round(x2, 2))

    with c2:
        st.metric("Joint 1 Y", round(y1, 2))
        st.metric("End Effector Y", round(y2, 2))

    st.subheader("⚙️ Current Parameters")
    st.write(f"**Link 1 Length:** {L1}")
    st.write(f"**Link 2 Length:** {L2}")
    st.write(f"**Joint 1 Angle θ1:** {theta1_deg}°")
    st.write(f"**Joint 2 Angle θ2:** {theta2_deg}°")

    st.subheader("📐 Forward Kinematics Equations")
    st.latex(r"x = L_1\cos(\theta_1) + L_2\cos(\theta_1 + \theta_2)")
    st.latex(r"y = L_1\sin(\theta_1) + L_2\sin(\theta_1 + \theta_2)")

with right_col:
    st.subheader("📊 Robotic Arm Visualization")

    fig, ax = plt.subplots(figsize=(7, 7))

    x_points = [x0, x1, x2]
    y_points = [y0, y1, y2]

    # Plot robotic arm
    ax.plot(x_points, y_points, marker="o", linewidth=4, label="Robotic Arm")

    # Plot points
    ax.scatter(x0, y0, s=120, label="Base")
    ax.scatter(x1, y1, s=120, label="Joint 1")
    ax.scatter(x2, y2, s=120, label="End Effector")

    # Workspace circle
    reach = L1 + L2
    workspace = plt.Circle((0, 0), reach, fill=False, linestyle="--", label="Workspace Boundary")
    ax.add_patch(workspace)

    # Axis settings
    ax.set_xlim(-reach - 2, reach + 2)
    ax.set_ylim(-reach - 2, reach + 2)

    ax.axhline(0)
    ax.axvline(0)
    ax.grid(True)
    ax.set_aspect("equal", adjustable="box")

    ax.set_title("2D Robotic Arm Workspace")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.legend(loc="upper right")

    st.pyplot(fig)

# Applications section
st.subheader("🚀 Applications")

st.write("""
This type of simulation is used in:

- Robotic arm motion analysis
- Pick-and-place robots
- Industrial manipulators
- Robot workspace visualization
- Motion planning
- Robotics education
""")

# Future improvements
st.subheader("🔧 Future Improvements")

st.write("""
- Add inverse kinematics
- Add 3-link robotic arm simulation
- Add animation between two positions
- Add obstacle avoidance in workspace
- Add pick-and-place path simulation
""")