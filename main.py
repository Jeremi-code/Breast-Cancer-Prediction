import numpy as np
import pickle
import streamlit as st
import re

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for input validation
def validate_input(value):
    if not value.strip():
        return False
    pattern = r'^[0-9]*\.?[0-9]+$'  # Allow positive numbers with or without decimals
    return value.strip() == '' or re.match(pattern, value.strip()) is not None

# creating a function for Prediction
def cancer_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'ይህ/ች ሰው Malignant ነው ወደ ካንሰርነት የመቀየር እድል አለው'
    else:
        return 'ይህ/ች ሰው Benign ነው ወደ ካንሰርነት የመቀየር እድል የለውም/ዝቅተኛ ነው'

def main():
    # giving a title
    st.sidebar.title("የጡት ካንሰር መለያ AI")
    selected_option=st.sidebar.selectbox("ተግባራትን ምረጥ", ("የካንሰር ምርምራ መትግበሪያ", "ስለ እኛ"))
    st.sidebar.write ("Repository:https://github.com/Jeremi-code/Breast-Cancer-Prediction")

    if  selected_option == "የካንሰር ምርምራ መትግበሪያ":

        st.title('የ ጡት ካንሰር ክላሲፊኬሽን AI መተግበሪያ')

        # getting the input data from the user
        radius_mean = st.text_input('የ እጢው ራዲየስ አማካይ ምን ያህል ነው?')
        texture_mean = st.text_input('ቴክስቸር አማካይ ስንት ነው?')
        perimeter_mean = st.text_input('ዙሪያ አማካይ ስንት ነው?')
        area_mean = st.text_input('ስፋት አማካይ ምን ያህል ነው?')
        smoothness_mean = st.text_input('የ ልስላሴ አማካይ ምን ያህል ነው?')
        compactness_mean = st.text_input('የ መጠቅጠቅ አማካይ ምን ያህል ነው?')
        concavity_mean = st.text_input('concavity_mean ምን ያህል ነው?')
        concave_points_mean = st.text_input('concave_points_mean ምን ያህል ነው?')
        symmetry_mean = st.text_input('ሳይሜትሪ አማካይ ምን ያህል ነው?')

        
        fractal_dimension_mean = st.text_input('ፍራክሽናል_ዳይሜንሽን_አማካይ ስንት ነው?')
        radius_se = st.text_input('ራዲየስ_ኤስኢ ስንት ነው?')
        texture_se = st.text_input('ቴክስቸር_ኤስኢ ምን ያህል ነው?')
        perimeter_se = st.text_input('ፐሪሜትር ኤስኢ ምን ያህል ነው?')
        area_se = st.text_input('ዔሪያ ኤስኢ ምን ያህል ነው?')
        smoothness_se = st.text_input('ስሙዝነስ ኤስኢ ምን ያህል ነው?')
        compactness_se = st.text_input('ኮምፓክትነስ ኤስኢ ምን ያህል ነው?')



        concavity_se = st.text_input('ኮኒኬቭ ኤስኢ ምን ያህል ነው?')
        concave_points_se = st.text_input('ኮኒኬቭ ፖይንትስ ኤሳኢ ስንት ነው?')
        symmetry_se = st.text_input('ሳይሜትሪ_ኤስኢ ስንት ነው?')
        fractal_dimension_se = st.text_input('ፍራክሽናል_ዳይሜንሽን_ኤስኢ ምን ያህል ነው?')
        radius_worst = st.text_input('ራዲየስ ዎርስት ምን ያህል ነው?')
        texture_worst = st.text_input('ቴክስቸር ዎርስት ምን ያህል ነው?')
        perimeter_worst = st.text_input('ፐሪሜትር ዎርስት ምን ያህል ነው?')
        area_worst = st.text_input('ኤሪያ ዎርስት ምን ያህል ነው?')

        smoothness_worst = st.text_input('ስሙዝነስ ዎርስት ምን ያህል ነው?')
        compactness_worst = st.text_input('ኮምፓክትነስ ዎርስት ስንት ነው?')
        concavity_worst = st.text_input('ኮንኬቪቲ ዎርስት ስንት ነው?')
        concave_points_worst = st.text_input('ኮኒኬቭ ፖይንትስ ዎርስት ምን ያህል ነው?')
        symmetry_worst = st.text_input('የ ሳይሜትሪ ዎርስት ምን ያህል ነው?')
        fractal_dimension_worst = st.text_input('የ ፍራክሽናል_ዳይሜንሽን_ዎርስት ምን ያህል ነው?')

        # validating input
        inputs = [radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]
        valid_inputs = all([validate_input(value) for value in inputs])

        # displaying the result
        if st.button('የካንሰር ምርመራ ዉጤት'):
            if valid_inputs:
                input_data = [float(value) if value.strip() != '' else 0.0 for value in inputs]
                prediction = cancer_prediction(input_data)
                st.success(prediction)
            else:
                st.error('ያስገቡት ባህርያት ትክክል አይደሉም!!! እባክዎ ትክክለኛ የሆነ ቁጥር ያስገቡ ፡፡ ')
    else:
        st.title("ስለ እኛ")
        st.write("<h5>ይህ መተግበሪያ በባህር ዳር ዩኒቨርስቲ በ3ኛ ዓመት የ ሶፍትዌር ኢንጂነሪንግ ተማሪዎች ተሰራ::ይህ መተግበሪያ ስትሪምሊት የተሰኘ ፍሬምወርክ ዩዘር ኢንትርፌስ ለመስራት ተጠቅመናል፡፡ ሞዴሉም የተሰራው Scikit learn ላይብራሪ ውስጥ በሚገኝ ሎጂስቲክ ሪግረሺን በተባለ ሞዴል ነው፡፡ በተጨማሪም pandas እና numpyን ለተለያዩ ጉዳዮች ተጠቅመናል ::</h5>", unsafe_allow_html=True)
        with st.container():
            st.subheader("የቡድን አባላት")
            st.markdown("<h6>1.ኤርምያስ ስንታየሁ</h6>",unsafe_allow_html=True)
            st.markdown("<h6>2.ዳግም ግዛቸው</h6>",unsafe_allow_html=True)
            st.markdown("<h6>3.ናትናኤል ቴዎድሮስ</h6>",unsafe_allow_html=True)
            st.markdown("<h6>4.ሜላት ተስፋዬ</h6>",unsafe_allow_html=True)
            st.markdown("<h6>5.ስማችው ገደፋው</h6>",unsafe_allow_html=True)


if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
  
    
  