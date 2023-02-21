import pandas as pd
import joblib
import streamlit as st

# Load the model
load_model = joblib.load('price_prediction_model.sav', mmap_mode ='r')

# Define the predict function
def predict_price(data):
    df = pd.DataFrame([data])
    preds = load_model.predict(df)
    return preds[0]

# Define the Streamlit app
def app():
    # Set the app title
    st.title('Real Estate Price Prediction')

    # Add input fields for the user to enter data
    province = st.selectbox('Province', ['Brussel','Antwerp','Brabant','West Flanders','East Flanders','Hainaut','Liège','Limburg','Namur'])
    zip_code = st.number_input('postal Code')
    building_type = st.selectbox('Building type', ['Apartment', 'House', 'Other'])
    bedroom = st.number_input('Number of rooms')
    land_surface = st.number_input('Land surface')
    heating_type = st.selectbox('Heating type', ['Gas', 'Electric', 'Other'])
    construction_year = st.number_input('Year of construction')

    # When the user clicks the 'Predict' button, run the predict_price function
    if st.button('Predict'):
        data = {
            'province': province.lower(),
            'zip': zip_code,
            'building_type': building_type.lower(),
            'bedroom': bedroom,
            'land_surface': land_surface,
            'heating_type': heating_type.lower(),
            'construction_Year': construction_year,
        }
        prediction = predict_price(data)
        st.success(f'The predicted price is €{prediction:.2f}')

# Run the app
if __name__ == '__main__':
    app()
