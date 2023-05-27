import streamlit as st
from PIL import Image
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('photo.jpg')


st.title('Выбери вкусняшку:)')
am = st.radio(
    "Что ты хотел бы скушать?",
    ('Сладкое', "Кислое", "Острое",'Солёное','Что-нибудь горячее', 'Что-нибудь Японское'))
if am == "Сладкое":
    sweet = st.radio(
        "Что бы ты хотел скушать сладкое?",
        ("Шоколад", "Мороженное", "Леденец", "Печеньку", "Тортик"))
    if sweet == 'Шоколад':
        st.write("Скушай шоколадку🍫")
        image = Image.open('shoco.png')
        st.image(image, caption ='Мне кажется, что «срок хранения» на шоколадках — это лишняя информация. Где это видано, чтобы шоколад ХРАНИЛСЯ?!            '
                                  '')

    if sweet == 'Мороженное':
        st.write("Скушай Мороженноe🍦")
        image = Image.open('ice_cream.jpg')
        st.image(image, caption= '— Я сегодня объеденно-недоеденная мороженками — Это как? — Физически нажралась… а теоретически ещё хочется))) ')

    if sweet == 'Леденец':
        st.write("Скушай Леденец🍭")
        image = Image.open('candy.jpg')
        st.image(image, caption='Чем занимаются родители в Новогоднюю ночь, когда их дети уже спят? Правильно — разбирают сладкие детские подарки и выбирают свои любимые конфеты ')


    if sweet == 'Печеньку':
        st.write("Скушай печеньку🍪")
        image = Image.open('cookies.jpg')
        st.image(image, caption='— Паап, печеньки закончились. чего ты так мало покупаешь?.. — Поставим вопрос по-другому. Чего ты так много жрёшь?! Вот это я называю правильный подход к жизни))))) ')


    if sweet == 'Тортик':
        st.write("Скушай Тортик🍰")
        image = Image.open('cake.jpg')
        st.image(image, caption='Пришла ко мне подруга чай пить… с тортиком. Я не успела даже глазом моргнуть, как она почему-то тортик не успела попробовать.)))')

elif am == 'Кислое':
    sour = st.radio(
        "Что бы ты хотел скушать кислое ?",
        ("Лимон", "Кислючку", "Мармеладки"))

    if sour == 'Лимон':
        st.write("Скушай Лимон🍋")
        image = Image.open('lemon.jpg')
        st.image(image, caption = 'В интернете написано, что лучшее средство от сонливости с самого утра - тёплая вода с лимоном. Лично я считаю, что лучшее средство от сонливости с утра - сон до обеда')


    if sour == 'Кислючку':
        st.write("Скушай Кислючку🍬")
        image = Image.open('sour_candies.jpg')
        st.image(image, caption=' когда уже придумают обертки для конфет, которые не шуршат!! а то палево…   ')


    if sour == 'Мармеладки🍡':
        st.write("Скушай Мармеладки")
        image = Image.open('marmalade.jpg ')
        st.image(image, caption='Шик с мармеладом уже не лечится, проверено.  ')

elif am == 'Солёное':
    salty = st.radio(
       "Что бы ты хотел скушать солёное ?",
        ("Чипсы", "Сухарики", "Рыбка"))

    if salty == 'Чипсы':
        st.write("Скушай Чипсы🧂")
        image = Image.open('chips.webp')
        st.image(image, caption=' Люди, когда вы едите чипсы, задумывались сколько там дряни в себя поглощаете? Я вот нет. Очень вкусно  ')

    if salty == 'Сухарики🍞':
        st.write("Скушай Сухарики")
        image = Image.open('crackers.jpg')
        st.image(image, caption='Хочу иметь такой же уровень иронии, как производители сухариков со вкусом красной икры.   ')

    if salty == 'Рыбка':
        st.write("Скушай Рыбку🐟")
        image = Image.open('fish2.jpg')
        st.image(image, caption=' Урок химии. Учитель: — Какие вещества не растворяются в воде? Вовочка, не задумываясь: — Рыбы!  ')

elif am == 'Что-нибудь горячее':
    Hot = st.radio(
       "Что бы ты хотел скушать горячее ?",
        ("Пицца", "Хачапури", "Бургер"))

    if Hot == 'Пицца':
        st.write("Скушай  пиццу🍕")
        image = Image.open('pizza.jpg')
        st.image(image, caption='Блондинка заказывает пиццу. На вопрос — на сколько частей разрезать: шесть или двенадцать — отвечает: — На шесть. Двенадцать мне не съесть.  ')

    if Hot == 'Хачапури':
        st.write("Скушай  Хачапури🫓")
        image = Image.open('khachapuri.jpg')
        st.image(image, caption='Когда тебя обманули и принесли хачапури без яйца    ')
    if Hot == 'Бургер':
        st.write("Скушай Бургер🍔")
        image = Image.open('burger.webp')
        st.image(image, caption='«Когда ты заказал в ресторане бургер, а твоя девушка сказала, что не голодна и попробует только пару кусочков картошки»    ')

elif am == 'Что-нибудь Японское':

    japanese = st.radio(
       "Что бы ты хотел скушать японское ?",
        ("Суши", "Поке", "Онигири"))
    if japanese == 'Суши':
        st.write("Съешь суши🍣")
        image = Image.open('sushi.jpg')
        st.image(image, caption='В суши—баре. — Будьте добры, роллы с лососем и вместо васаби чилийский хрен... — Хрен вам, а не васаби... Я правильно записал?  ')


    if japanese == 'Поке':
        st.write("Съешь Поке🍱")
        image = Image.open('poke.jpg')
        st.image(image, caption='🍱  Самое аппетитное поке')

    if japanese == 'Онигири':
        st.write("Съешь  Онигири🍙")
        image = Image.open('onigiri.jpg')
        st.image(image, caption='🍙   Самые аппетитные Онигири')



else:
    st.write('Купите себе дошик🍜')
    image = Image.open('doshirak.jpg ')
    st.image(image, caption='Бывает, чуть-чуть передержишь — и всё, доширак уже не альденте.  ')
