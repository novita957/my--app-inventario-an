import streamlit as st

# Definir el inventario inicial en un diccionario
inventario = {
    "bebida": 5,
    "galletas": 10,
    "harina": 4,
    "arroz": 10
}

# Configuración de la página
st.set_page_config(page_title="Control de Inventario", page_icon="📦")

st.title("📦 Control de Inventario")
st.write("Consulta de manera rápida la disponibilidad de tus productos.")

# Mostrar el inventario actual de forma visual
st.subheader("Inventario Actual")
for producto, cantidad in inventario.items():
    st.write(f"- **{producto.capitalize()}**: {cantidad} unidades")

st.markdown("---")

# Caja de texto para realizar la pregunta
st.subheader("Buscar Producto")
consulta = st.text_input("¿Qué producto deseas consultar? (Ej: bebida, galletas, harina, arroz)")

# Lógica de búsqueda
if consulta:
    # Convertir a minúsculas para evitar problemas de formato
    producto_buscado = consulta.strip().lower()
    
    if producto_buscado in inventario:
        cantidad = inventario[producto_buscado]
        st.success(f"Sí, hay **{producto_buscado}**. Actualmente tenemos **{cantidad}** unidades en existencia.")
    else:
        st.error(f"Lo sentimos, el producto '{consulta}' no existe en el inventario o no está registrado.")
