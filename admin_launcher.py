import streamlit as st
import streamlit_authenticator as stauth
#import hm_methods as hmm
import yaml
from yaml.loader import SafeLoader

import hm_methods as hmm


st.set_page_config(page_title="Login page", page_icon=":hospital:", layout="wide")
st.title(':hospital: Hospital Management App')
st.write('Admin Login page')


# with open('config.yaml') as authstream:
#     config = yaml.load(authstream, Loader=SafeLoader)

authenticator = stauth.Authenticate(config['credentials'], 
                                    config['cookie']['name'], 
                                    config['cookie']['key'], 
                                    config['cookie']['expiry_days'], 
                                    config['preauthorized']
                                    )

# name, authentication_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    # st.write("DEBUG: st.session_state['authentication_status'] -> ", st.session_state["authentication_status"])
    # authenticator.logout('Logout', 'main', key='logout_btn')
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome 🌟 *{name}* 🌟')
    st.title('random title ')
elif st.session_state["authentication_status"] is False:
    # st.write("DEBUG: st.session_state['authentication_status'] -> ", st.session_state["authentication_status"])
    st.error("incorrect credentials", icon="🚨")
elif st.session_state["authentication_status"] is None:
    st.warning("Credentials are empty, Please enter credentials first", icon="🤖")





st.markdown("""    © Evaluation Nerds Mar-2023""" )