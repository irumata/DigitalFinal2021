import streamlit as st
import sys
sys.path.append("./Streamlit-Authenticator")
import streamlit_authenticator as stauth
#from Streamlit-Authenticator import streamlit_authenticator as stauth

import time
import paginator
import image_paginator
import joblib
st.set_page_config( page_title="Витрина решений", page_icon="/home/nknyazev/projects/DigitalFinalHack2021/logo_circle.png", layout="wide",)
from streamlit_text_rating.st_text_rater import st_text_rater

import re
import random
import json
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

import requests
  
# Making a get request
#r#esponse = #requests.get('http://127.0.0.1:5000/grab/visorlabs')
import sc
# print response
st.sidebar.image("logo_long_trans.png")


names = ['Nick','user',"testuser"]
usernames = ['Nick','user',"testuser"]
passwords = ['123','468',"4680"]

hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Вход','sidebar')

data_all,color_list = joblib.load("data.j")
tegs = list(color_list.keys())



if authentication_status == False:
    st.error('Неверный пароль или имя пользователя')
    st.stop()
if authentication_status == None:
    
    st.title("Рассказать о своем проекте")
    if 'first_button' not in st.session_state:
        st.session_state['first_button'] = False
    if not  st.session_state['first_button']:
        container_intro =st.container()
        email = container_intro.text_input(label = "Электронная почта",placeholder="электронна почта")
        but_res =  container_intro.button("Заполнить заявку")
        if "@" in email:
            st.session_state['first_button'] = but_res
        elif but_res:
            st.warning('Введите корректный адрес электронной почты')
            
    else:
        opis = st.text_area(label="Краткое описание",placeholder="Краткое описание вашего решения")
        site = st.text_input(label="сайт",placeholder="адрес сайта")
        polzs = st.text_area(label="польза продукта",placeholder="Опишите пользу от вашего продукта")
        org_interse = st.selectbox(label="организация московского транспорта, интересная в первую очередь",options=["Не знаю","Московский метрополитен","МосГорТранс","ГИБДД"], index=0)
        zapros = st.text_area(label="запрос к акселератору и видение пилотного проекта",
                              placeholder="Какой запрос к акселератору")
        inn = st.text_input(label="инн юридического лица",placeholder="ИНН")
        where_know = st.selectbox(label=  'откуда о нас узнали',options=["СМИ","Друзья","Коллеги","Интернет"])
        phone= st.text_input(label= 'контактный телефон +7',placeholder="XXXXXXXXXX")
        dolg= st.text_input(label=  'должность контактного лица')
        present =  st.text_area(label='ссылка на презентацию')
        but_res_end =  st.button("Отправить заявку")
        if but_res_end:
            st.title("Спасибо, мы с вами свяжемся")



    
   # st.warning('Заполните поля для входа')
   # st.error('Поля не заполнены')
    st.stop()

    
#if authentication_status:
s1,s2 = st.columns(2)
s1.write('Пользователь *%s*' % (name))
s2.image("logo_quad.png",width=150)


query_params = st.experimental_get_query_params()
in_index = 1
if "proj" in query_params.keys():
    in_index=2
    proj = query_params["proj"]
    

menu_ind = st.sidebar.selectbox(
    "Раздел",
    options=['Личный кабинет', 'Поиск решений', 'Карточка организации'],
index=in_index)

if menu_ind=='Поиск решений':
    #s1,s2,s3 = st.columns([1,1,1])
    s1.title('Поиск решений')
    #s2.image("logo_circle.png",width=200)

    tags = {"Технологические направления":{
       "городской транспорт": ["метро","наземный","обратная связь","остановки"],
        "мобильность":["зарядные пункты","вода","беспилотники"],
        "безопасность":["прогноз ДТП","предотврашение ДТП"],
        "Экология":["велосипеды"],
        "Цифровизация":["парковки","мобильные технологии"]    
    }
              }
    naprs = tags[list(tags.keys())[0]]
    first_level_name = list(tags.keys())[0]
    if 'first_level_select' not in st.session_state:
        st.session_state['first_level_select'] = list(naprs.keys())[:2]

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
    possible_tags = tegs+possible_tags
    if 'second_level_select' not in st.session_state:
        st.session_state['second_level_select'] = possible_tags[:10]
    def_list_sec =  st.session_state['second_level_select']

    def_list_sec = [d for d in def_list_sec if d in possible_tags]
    with col2:
        second_level_select = st.multiselect(label="Тэги",options=possible_tags+["все"],default=possible_tags[:10],
                            on_change=on_change_first_level_select, key="first_level_select_w2")
    st.session_state['second_level_select']=second_level_select
    if "все" in first_level_select:
        second_level_select =  [i for napr in first_level_select for i in naprs[napr] ]





    with st.spinner('Поиск решений...'):
        if req !="":
            api_url = 'http://31.134.186.2:5000/search'

            req = {'top_n': '10', 
       'max_dist': '3',
       'request':req}

            r = requests.post(url=api_url, json=req)
            result = json.loads(r.text)
            #time.sleep(0)

    if req=="" :
        st.stop()

    start_color, end_color = st.select_slider(
         "Уровень решения",
         options=['скрининг', 'скоринг', 'экспертный совет', 'акселлерационная программа', 'программа пилотирования', 'инвестирование','готовый продукт'],
         value=('скрининг', 'готовый продукт'),
        help= "выберете уровень решения")
    cards = []
    col_res1, col_res2 = st.columns(2)

    long_list = []
    
    all_items = sorted(result.items(),key=lambda x: x[1],reverse=False)
    for name, rat in all_items:
        fix_name=name.lower().replace(" ","_").replace("й","и").strip()
        res_row=data_all.set_index("Имя").loc[fix_name]
        #st.write(fix_name)
       # st.write(str(res_row))
        long_list.append( (res_row,1/rat,fix_name))


    detail_list = []
    i=-1
    for row,rating,fix_name in long_list: 
        i+=1
        #st.write(row)
        r = dict(row)
        
        tegs_st = [tg for tg in tegs if r[tg]==True]
        if "все" in second_level_select:
            
            found_tags = tegs_st+[""]
        else:
            found_tags=[t for t in tegs_st if t in second_level_select]
        if len(found_tags)<1:
            i-=1
            continue

        
        
        
        if i%2 ==0:
            col_res1, col_res2 = st.columns(2)


            cont = col_res1.expander(r["наименование команды/организации"]+"    соотвествие: "+str(rating)[:5])
        else:
            cont = col_res2.expander(r["наименование команды/организации"]+"    соотвествие: "+str(rating)[:5])

        with cont:
            st.caption(r['краткое описание продукта'])
            #st.сaption(r['краткое описание продукта'])
            if len(r["сколько человек в организации"]) >1:
                emp_count = int(re.search(r'\d+', r["сколько человек в организации"]).group())
            else:
                emp_count=15
            emp_count_dir = 1-2*(len(r['краткое описание продукта'])%2)
            emp_count_ch = len(r['краткое описание продукта'])%4+1
            delta=f"{emp_count_ch*emp_count_dir} за месяц"
            test_str = r['запрос к акселератору и видение пилотного проекта']
            proj_name = fix_name
            
            st.markdown(f"[карточка проекта](http://ailine.softline.com:8501/?proj={proj_name.lower()})")
            tegs_line = '<span style="color:#ffffff">g</span>'.join(f'<span style="color:{color_list[tg]};background_color:{color_list[tg]}">d</span><span style="background_color:{color_list[tg]}">{tg}</span><span style="color:{color_list[tg]};background_color:{color_list[tg]}">d</span>  ' for tg in tegs_st)
            st.markdown(  tegs_line      
                      , unsafe_allow_html=True)

            # if len(test_str) <1:
            #     test_str="2"*random.randint()
            # #overcome =  l(re.search(r'\d+', ).group())*1000
            # count_dir = 1-2*(len(r['запрос к акселератору и видение пилотного проекта'])%2)
            # count_ch = len(r['запрос к акселератору и видение пилотного проекта'])%4+1
            #overcome_delta=f"{count_ch*count_dir} за месяц"




    #     if i%2==0:
    #         detail_list.append([[emp_count,delta],[]])
    #     else:
    #         col_res1, col_res2 = st.columns(2)



            feedback_proj = st_text_rater(text="Проект релевантен?",key=f"resp_proj{i}")

    ##
        cards.append(cont)
    response_all = st_text_rater(text="Была ли подборка полезной?", key="resp_end") 

    
    
##################


if menu_ind=='Карточка организации':
    in_index_p=0
    val_list = [""]+data_all["Имя"].tolist()
    if "proj" in query_params.keys():
        proj = query_params["proj"][0].lower()
        in_index_p = val_list.index(proj)
    
    proj = st.sidebar.selectbox(label="имя проекта", options=val_list,index=in_index_p)
    if proj=="":
        st.stop()

    
    r = data_all.set_index("Имя").loc[proj]
    proj_name = r['наименование команды/организации']

    st.title('Карточка организации '+proj_name)


    st.caption(r['краткое описание продукта'])
            #st.сaption(r['краткое описание продукта'])
    emp_count = int(re.search(r'\d+', r["сколько человек в организации"]).group())
    emp_count_dir = 1-2*(len(r['краткое описание продукта'])%2)
    emp_count_ch = len(r['краткое описание продукта'])%4+1
    delta=f"{emp_count_ch*emp_count_dir} за месяц"
    test_str = r['запрос к акселератору и видение пилотного проекта']
    
    
    
    
    cl1,cl2 = st.columns(2)
    v = "фио контактного лица по заявке"
    cl1.markdown(v+': **'+r[v]+"**")


    v = "должность контактного лица"
    cl2.markdown(f"{v}: **{r[v]} **")
    v = "контактный телефон"
    cl1.markdown(f"{v}: **{r[v]} **")
    v = "контактная почта"
    cl2.markdown(f"{v}: **{r[v]} **")
    v = "сайт"
    cl1.markdown(f"{v}: **{r[v]} **")
    v = "ссылка на презентацию"
    cl2.markdown(f"{v}: **{r[v]} **")             
    smi  = sc.search_info("visorlabs")
    smi = smi.replace("\n","\n\n")
    st.subheader("Информация из СМИ")
    st.write(smi)
    st.subheader("Бета версия сбора информации")
    cl1,cl2 = st.columns(2)


    cl1.metric("Сотрудников", emp_count, delta=f"{emp_count_ch*emp_count_dir} за месяц", delta_color="normal")
    test_str=r['запрос к акселератору и видение пилотного проекта']
    if len(test_str) <1:
        test_str="2"*random.randint()
    overcome =  len(test_str)*1000
    count_dir = 1-2*(len(r['запрос к акселератору и видение пилотного проекта'])%2)
    count_ch = len(r['запрос к акселератору и видение пилотного проекта'])%4+1
    overcome_d=f"{count_ch*count_dir} за месяц"
    cl2.metric("Оборот", overcome, delta=overcome_d, delta_color="normal")



            # if len(test_str) <1:
            #     test_str="2"*random.randint()
            # #overcome =  l(re.search(r'\d+', ).group())*1000
            # count_dir = 1-2*(len(r['запрос к акселератору и видение пилотного проекта'])%2)
            # count_ch = len(r['запрос к акселератору и видение пилотного проекта'])%4+1


    

#with st.form("my_form"):

#paginator.demonstrate_paginator(on_sidebar=False)
#image_paginator.demonstrate_image_pagination()
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

