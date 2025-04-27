import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="📊 Gra w Marżę i Koszty", layout="centered")
st.title("📊 Sprawdź ile zarobi firma!")

st.markdown("**Ustaw parametry swojego biznesu i zobacz, jak zmieniają się przychody i zyski!**")

# Suwaki
price = st.slider("💰 Cena za sztukę", 1, 100, 30)
cost = st.slider("🛠 Koszt jednostkowy", 1, price, 15)
quantity = st.slider("📦 Liczba sprzedanych sztuk", 0, 1000, 300)

# Obliczenia
revenue = price * quantity
total_cost = cost * quantity
profit = revenue - total_cost

# Wykres
fig = go.Figure()
fig.add_trace(go.Bar(x=["Przychód", "Koszt", "Zysk"],
                     y=[revenue, total_cost, profit],
                     marker_color=["green", "red", "blue"]))

fig.update_layout(title="📈 Wyniki finansowe Twojej firmy", yaxis_title="Kwota (zł)")

# Wyniki
st.plotly_chart(fig)
st.markdown(f"✅ **Przychód:** {revenue} zł")
st.markdown(f"❌ **Koszt całkowity:** {total_cost} zł")
st.markdown(f"💸 **Zysk:** {profit} zł")

