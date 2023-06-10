    # -*- coding: utf-8 -*-
import numpy as np
import pickle 
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def cancer_prediction(input_data):
    # input_data=[]

    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data,dtype=np.float64)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'ይህ/ች ሰው Malignant ነው ወደ ካንሰርነት የመቀየር እድል አለው'
    else:
      return ' ይህ/ች ሰው Benign ነው ወደ ካንሰርነት የመቀየር እድል የለውም/ዝቅተኛ ነው'
  
    
  
def main():
    
    
    # giving a title
    st.title('የ ጡት ካንሰር ክላሲፊኬሽን AI መተግበሪያ, ባህር ዳር ዩኒቨርሲቲ')
    
    
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
   
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('የ ካንሰር ምርመራ ዉጤት'):
        diagnosis = cancer_prediction([radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst])
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  