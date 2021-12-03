import streamlit as st
import sys
sys.path.append("./Streamlit-Authenticator")
import streamlit_authenticator as stauth
#from Streamlit-Authenticator import streamlit_authenticator as stauth

import time

import joblib
st.set_page_config( page_title="Витрина решений", page_icon="/home/nknyazev/projects/DigiHack2021/logo.png", layout="wide",)
from streamlit_text_rating.st_text_rater import st_text_rater

import re
import random

import streamlit as st
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #019895;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #449895;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True)


names = ['Nick','user']
usernames = ['Nick','user']
passwords = ['123','468']

hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Вход','sidebar')


if authentication_status == False:
    st.error('Неверный пароль или имя пользователя')
    st.stop()
if authentication_status == None:
    st.warning('Заполните поля для входа')
    st.error('Поля не заполнены')
    st.stop()

    
#if authentication_status:
st.write('Пользователь *%s*' % (name))
st.title('Поиск решений')

tags = {"Технологические направления":{
   "городской транспорт": ["метро","назменый","обратная связь","остановки"],
    "мобильность":["зарядные пункты","вода","беспилотники"],
    "безопасность":["прогноз ДТП","предотврашение ДТП"],
    "Экология":["велосипеды"],
    "Цифровизация":["парковки","мобильные технологии"]    
}
          }
naprs = tags[list(tags.keys())[0]]
first_level_name = list(tags.keys())[0]
if 'first_level_select' not in st.session_state:
    st.session_state['first_level_select'] = []
if 'second_level_select' not in st.session_state:
    st.session_state['second_level_select'] = []
def on_change_first_level_select():
    if "все" in first_level_select:
        st.session_state['first_level_select']=["все"] 
def_list =  st.session_state['first_level_select']
req = st.text_input( label="",placeholder='Текст запроса')









    
with st.expander("Направления поиска",expanded=True):


    col1, col2 = st.columns(2)


with col1:
    first_level_select = st.multiselect(label=first_level_name,default=def_list,options=list(naprs.keys())+["все"],
                        on_change=on_change_first_level_select, key="first_level_select_w")
if "все" in first_level_select:
    first_level_select = list(naprs.keys())

possible_tags = [i for napr in first_level_select for i in naprs[napr] ]
def_list =  st.session_state['second_level_select']

def_list = [d for d in def_list if d in possible_tags]
with col2:
    second_level_select = st.multiselect(label="Тэги",options=possible_tags+["все"],default=def_list,
                        on_change=on_change_first_level_select, key="first_level_select_w2")
st.session_state['second_level_select']=second_level_select
if "все" in first_level_select:
    second_level_select =  [i for napr in first_level_select for i in naprs[napr] ]





with st.spinner('Поиск решений...'):
    if req !="":
        time.sleep(0)

if req=="" and False:
    st.stop()
    
start_color, end_color = st.select_slider(
     "Уровень решения",
     options=['заявка', 'идет тестирование', 'успешное тестирование', 'идет внедрение', 'успешное внедрение', 'массовое производство'],
     value=('заявка', 'массовое производство'),
    help= "выберете уровень решения")
data_all = joblib.load("data.j")
cards = []
col_res1, col_res2 = st.columns(2)

long_list = []
for i,row in enumerate(data_all.iterrows()):
    long_list.append((i,row))
for i,row in enumerate(data_all.iterrows()):
    long_list.append((i+2,row))

detail_list = []
for i,row in long_list:
    r = dict(row[1])
    if i%2 ==0:
        col_res1, col_res2 = st.columns(2)


        cont = col_res1.expander(r["наименование команды/организации"])
    else:
        cont = col_res2.expander(r["наименование команды/организации"])


    with cont:
        st.caption(r['краткое описание продукта'])
        #st.сaption(r['краткое описание продукта'])
        emp_count = int(re.search(r'\d+', r["сколько человек в организации"]).group())
        emp_count_dir = 1-2*(len(r['краткое описание продукта'])%2)
        emp_count_ch = len(r['краткое описание продукта'])%4+1
        delta=f"{emp_count_ch*emp_count_dir} за месяц"
        test_str = r['запрос к акселератору и видение пилотного проекта']
        st.metric("Сотрудников", emp_count, delta=f"{emp_count_ch*emp_count_dir} за месяц", delta_color="normal")


        if len(test_str) <1:
            test_str="2"*random.randint()
        #overcome =  l(re.search(r'\d+', ).group())*1000
        count_dir = 1-2*(len(r['запрос к акселератору и видение пилотного проекта'])%2)
        count_ch = len(r['запрос к акселератору и видение пилотного проекта'])%4+1
        #overcome_delta=f"{count_ch*count_dir} за месяц"



        
#     if i%2==0:
#         detail_list.append([[emp_count,delta],[]])
#     else:
#         col_res1, col_res2 = st.columns(2)


            
        response = st_text_rater(text="Проект релевантен?",key=f"resp_proj{i}")

##
    cards.append(cont)
response_all = st_text_rater(text="Была ли подборка полезной?", key="resp_end")   
##################
#with st.form("my_form"):


   # st.write("Inside the form")
   # slider_val = st.slider("Form slider")
    #checkbox_val = st.checkbox("Form checkbox")
    # Every form must have a submit button.
    # submitted = st.form_submit_button("Submit")
    # if submitted: 
    #     pass
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
# if st.session_state['authentication_status']:
#     st.write('Welcome *%s*' % (st.session_state['name']))
#     st.title('Some content')
# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state['authentication_status'] == None:
#     st.warning('Please enter your username and password')
