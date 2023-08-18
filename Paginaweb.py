import streamlit as st
import requests
import urllib.parse

# Ruta de la imagen que deseas mostrar
imagen_ruta = 'logo.png'




# Usar st.image para mostrar la imagen en la parte superior izquierda
st.image(imagen_ruta)
#st.image(imagen_ruta, width=400)


BASE_URI = "https://prueba13ago2023.onrender.com/"

def consulta(user_id):
    url = urllib.parse.urljoin(BASE_URI, f"/recomendacion/{user_id}")
    #url = f"https://julio-mlops2.onrender.com/peliculas_mes/{mes}
    r = requests.get(url).json()
    return r


st.title("Página de Inicio de Sesión")
    
# Obtener nombre de usuario y contraseña
username = st.text_input("Nombre de Usuario")
password = st.text_input("Contraseña", type="password")

recomendacion = consulta(username)

# Verificar las credenciales
if password == "" or password == " ":
    st.success("Ingrese su usuario y contraseña")
elif username == username and password == username:
    st.success(f"Bienvenido, {username}! de acuerdo a tus gustos tenemos la siguiente recomendacion:")
    st.success(list(recomendacion.values())[0])
else:
    st.error("Credenciales incorrectas")

#elif username != "" or password != "":
 #   st.error("Credenciales incorrectas")

