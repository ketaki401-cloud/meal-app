import streamlit as st
import google.generativeai as genai


# Setup the AI Chef
genai.configure(api_key="AIzaSyBmtRnRiyFKvaNJyGiwCC9WHJKtPWDi4nE")
model = genai.GenerativeModel('gemini-1.5-flash')
if "selection" not in st.session_state:
    st.session_state.selection = None


def get_ai_recipe(dish_name):
         
     prompt=f"""
        You are a friendly Maharashtrian chef who loves sharing culinary secrets.
        Write a traditional recipe for {dish_name} with a 'foodie' vibe.
        Structure the response with these exact headers:
        
        ### 🌟 Why We Love It
        (A one-sentence 'foodie' description of the dish)
        
        ### 🛒 The Essentials
        (List of ingredients with measurements)
        
        ### 👨‍🍳 The Method
        (3-4 simple cooking steps)
        
        ### 🤫 The Secret Tip
        (One specific pro-tip or 'Aaji's secret' to make it extra authentic)
        """


     response = model.generate_content(prompt)    
     return response.text

# Setup the page look
st.set_page_config(page_title="Maharashtra AI Meal Planner", layout="wide")

# Custom Styling for an "Attractive" Look    
st.markdown("""
<style>
.main { background-color: #FFF9F5; }
</style>
""",unsafe_allow_html=True)

st.title("🗺️ Maharashtra Regional AI Meal Planner")
st.write("Click a region pin to discover local refreshments, meals, and sweets!")

# Your Regional Data
data = {
    "Konkan 🌊": {
        "Refreshment": "🥤 Solkadhi (🌿 Vegan | 10m) - *Tip: Use Cranberry + Lime if Kokum is missing.*",
        "Main Dish": "🥘 Malvani Fish Curry (🔴 Non-Veg | 40m)",
        "Sweet": "🍮 Ukadiche Modak (🟢 Veg | 45m)",
        "Shelf-Life": "📦 Phanas Poli (🌿 Vegan | 20m)"
    },
    "Vidarbha 🔥": {
        "Refreshment": "🥤 Mattha (🟢 Veg | 5m) - *Tip: Use Greek Yogurt thinned with water.*",
        "Main Dish": "🥘 Saoji Chicken (🔴 Non-Veg | 50m)",
        "Sweet": "🍮 Santra Barfi (🟢 Veg | 20m)",
        "Shelf-Life": "📦 Mirchi Locha (🌿 Vegan | 15m)"
    },
    "Khandesh 🥜": {
        "Refreshment": "🥤 Khandeshi Chai (🟢 Veg | 10m)",
        "Main Dish": "🥘 Shev Bhaji (🟢 Veg | 25m) - *Tip: Use spicy pretzels for crunch abroad!*",
        "Sweet": "🍮 Mande (🟢 Veg | 60m)",
        "Shelf-Life": "📦 Bibadi (🌿 Vegan | 30m)"
    },
    "Western MS 🌾": {
        "Refreshment": "🥤 Piyush (🟢 Veg | 10m)",
        "Main Dish": "🥘 Misal Pav (🟢 Veg | 35m) - *Tip: Use Brown Lentils if Moth beans aren't found.*",
        "Sweet": "🍮 Puran Poli (🟢 Veg | 50m)",
        "Shelf-Life": "📦 Bakarwadi (🟢 Veg | 40m)"
    }
}

# Regional Pins (Interactive Buttons)
col1, col2, col3, col4 = st.columns(4)
with col1: k_pin = st.button("📍 Konkan")
with col2: v_pin = st.button("📍 Vidarbha")
with col3: kh_pin = st.button("📍 Khandesh")
with col4: w_pin = st.button("📍 Western MS")
if k_pin: st.session_state.selection = "Konkan 🌊"
elif v_pin: st.session_state.selection = "Vidarbha 🔥"
elif kh_pin: st.session_state.selection = "Khandesh 🥜"
elif w_pin: st.session_state.selection = "Western MS 🌾"
selection = st.session_state.selection
# Now, we pull the value out of memory to use for the rest of the app
selection = st.session_state.selection

if selection:
    st.divider()
    st.header(f"Results for {selection}")
    items = data[selection]
    
# Create 4 columns for the 4 categories
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.info(f"**Refreshment**\n\n{items['Refreshment']}")
        with st.expander("Get Recipe ✨"):
            if st.button("Generate", key=f"btn_{selection}_ref"):
                with st.spinner("Writing..."):
                    st.write(get_ai_recipe(items['Refreshment']))

    with c2:
        st.success(f"**Main Dish**\n\n{items['Main Dish']}")
        with st.expander("Get Recipe ✨"):
            if st.button("Generate", key=f"btn_{selection}_main"):
                with st.spinner("Writing..."):
                    st.write(get_ai_recipe(items['Main Dish']))

    with c3:
        st.warning(f"**Sweet Dish**\n\n{items['Sweet']}")
        with st.expander("Get Recipe ✨"):
            if st.button("Generate", key=f"btn_{selection}_sweet"):
                with st.spinner("Writing..."):
                    st.write(get_ai_recipe(items['Sweet']))

    with c4:
        st.error(f"**Shelf-Life**\n\n{items['Shelf-Life']}")
        with st.expander("Get Recipe ✨"):
            if st.button("Generate", key=f"btn_{selection}_shelf"):
                with st.spinner("Writing..."):
                    st.write(get_ai_recipe(items['Shelf-Life']))
else:
    st.info("Tap a location pin on the map (the buttons above) to start exploring!")

 




 
