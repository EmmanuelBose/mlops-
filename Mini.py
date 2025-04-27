import streamlit as st
import pickle
import os

def get_hardness():
    return st.text_input("HARDNESS")

def get_toughness():
    return st.text_input("TOUGHNESS")

def get_density():
    return st.text_input("DENSITY")

def get_yield_stress():
    return st.text_input("YIELD STRESS")

def predict_apps(h, t, d, ys):
    model_path = 'mini_project_model.pkl'
    if not os.path.exists(model_path):
        st.error(f"Model file '{model_path}' not found! Please upload it to the app directory.")
        return
    
    try:
        with open(model_path, 'rb') as file:
            loaded_model = pickle.load(file)
        new_data = [[float(h), float(t), float(d), float(ys)]]
        prediction = loaded_model.predict(new_data)
        st.success("Prediction Successful!")
        st.write("Prediction with new data:")
        st.write(prediction)
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# --------- Streamlit App Start ----------
st.title('PREDICTION OF APPLICATION USE OF MATERIALS')

# Display image if available
if os.path.exists('app.png'):
    st.image('app.png')
else:
    st.warning("App image not found. Please upload 'app.png'.")

# Get user inputs
hardness_value = get_hardness()
toughness_value = get_toughness()
density_value = get_density()
yield_stress_value = get_yield_stress()

st.write("The parameters you entered are:")
st.write(f"Hardness: {hardness_value}")
st.write(f"Toughness: {toughness_value}")
st.write(f"Density: {density_value}")
st.write(f"Yield Stress: {yield_stress_value}")

# Predict button
if st.button("Predict"):
    if hardness_value and toughness_value and density_value and yield_stress_value:
        predict_apps(hardness_value, toughness_value, density_value, yield_stress_value)
    else:
        st.warning("Please enter all values before predicting.")

