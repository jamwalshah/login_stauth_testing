import streamlit as st
import streamlit_authenticator as stauth
import hm_methods as hmm
import yaml
from yaml.loader import SafeLoader

# import hm_methods as hmm



st.set_page_config(page_title="Login page", page_icon=":hospital:", layout="wide")
st.title(':hospital: Hospital Management App')
st.write('Login page')


with open('config.yaml') as authstream:
    config = yaml.load(authstream, Loader=SafeLoader)

authenticator = stauth.Authenticate(config['credentials'], 
                                    config['cookie']['name'], 
                                    config['cookie']['key'], 
                                    config['cookie']['expiry_days'], 
                                    config['preauthorized']
                                    )

name, authentication_status, username = authenticator.login('Login', 'main')

# st.write("DEBUG: st.session_state -> ", st.session_state)

if st.session_state["authentication_status"]:

    # st.write("DEBUG: authentication_status -> ", authentication_status)
    # st.write("DEBUG: st.session_state['authentication_status'] -> ", st.session_state["authentication_status"])
    # authenticator.logout('Logout', 'main', key='logout_btn')
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome 🌟 *{name}* 🌟')
    # st.write(f'Role is 🌟 *{role}* 🌟') // tried to make it role based, but authenticator.login() does not retrun custom fields
    st.title('random title ')
elif st.session_state["authentication_status"] is False:
    # st.write("DEBUG: st.session_state['authentication_status'] -> ", st.session_state["authentication_status"])
    st.error("incorrect credentials", icon="🚨")
elif st.session_state["authentication_status"] is None:
    st.warning("Credentials are empty, Please enter credentials first", icon="🤖")


## check DB connectivity
# hmm.check_db_connectivity() #un-comment to enable checking db connectivity

## selct DB
# hmm.show_db()               #un-comment to enable printing db

## create tables
hmm.create_table()

## initialize users
# hmm.initialize_users()     #un-comment to enable creating users

## show created tables
# hmm.show_users()           #un-comment to enable printing users

## initialize doctors
# hmm.insert_default_doctors_nurses()   #un-comment to enable inserting default doctors & nurses

## show created tables
# hmm.show_tables()          #un-comment to enable printing tables





st.markdown("""    © Evaluation Nerds Mar-2023""" )