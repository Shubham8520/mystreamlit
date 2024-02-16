import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://images.jdmagicbox.com/comp/def_content/film_production_houses/default-film-production-houses-6.jpg?clr=#808080')
st.title('SB Productions')
st.header('By Shubham')
st.text('Give urself a chance to ACT')
if(mymenu=='Home'):
    st.markdown('<center><h1>HELLO ACTOR</h1><center>',unsafe_allow_html=True)
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input("Choose Date of Birth")
        age=st.slider('Choose age')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name:',name,'DOB:',dob,'Age:', age)

elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','Hello this is the downloaded data','Film list.txt' )
    
    
