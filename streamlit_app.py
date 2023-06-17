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

streamlit.header("View our fruit list - Add your favourites!:")
def get_fruit_load_list():
       with my_cnx.cursor()as my_cur:
              my_cur.execute("SELECT * from fruit_load_list")
              return my_cur.fetchall()
if streamlit.button ('Get Fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
       my_cnx.close ()
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
#Allow the end user to add fruits to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit
    
add_my_fruit = streamlit.text_input('What fruit would you like to add?')   
if streamlit.button('Add a Fruit to the List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
       my_cnx.close ()
      back_from_function = insert_row_snowflake(add_my_fruit)
      streamlit.text(back_from_function)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor()as my_cur:
      my_cur.execute("insert into fruit_load_list values ('" +"jackfruit", "papaya", "guava" and "kiwi" +"')")
      return "Thanks for adding" + new_fruit
