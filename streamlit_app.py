import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title ('my parents new healthy dinner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruit_loadlist():
  with my_cur = my_cnx.cursor() as my_cur():
  my_cur.execute("SELECT * from fruit_load_list")
  return mychar.fetchall()

streamlit.header('Fruityvice Fruit Advice!')
if streamlit.button ('Get Fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_loadlist()
  streamlit.dataframe(my_data_rows)
except URLError as e:
  
  streamlit.stop()


Add_my_fruit = streamlit.text_input('What fruit would you like add?','Kiwi')
streamlit.write('Thanks for adding',Add_my_fruit)

my_cur.execute ("insert into fruit_load_list values ('from streamlit')")

