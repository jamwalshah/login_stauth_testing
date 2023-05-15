# import streamlit as st
import streamlit_authenticator as stauth
# # run htis as a separate python file to generate hashed passwords
# passwds=['admin','surya','swapnil','vaibhav','tejaswini','usha','ushashree']
# hashed_passwords = stauth.Hasher(passwds).generate()
# print(type(hashed_passwords)) # debug
# print(hashed_passwords) # debug
# for i in range(len(hashed_passwords)):
#     print(passwds[i], "-> ", hashed_passwords[i])

print()
# hashed_passwords = stauth.Hasher(['admin123', 'surya123', 'swapnil123']).generate()
passlist=['admin123', 'doctor123', 'nurse123','surya123','swapnil123','vaibhav123','tejaswini132','usha123','ushashree123']
hashed_passwords = stauth.Hasher(passlist).generate()
for ele in hashed_passwords:
    print(ele)
# print(hashed_passwords)
print()

print("admin pass:  ", stauth.Hasher(['admin123']).generate())
print("doctor pass: ", stauth.Hasher(['doctor123']).generate())
print("nurse pass:  ", stauth.Hasher(['nurse123']).generate())




print("""    © Evaluation Nerds Mar-2023""" )