# Air-Quality-Yes, the air quality in North India is generally worse than in South India. This is due to a combination of factors, including higher population density, more intense industrial activity, and seasonal factors like stubble burning in the north. [1, 2, 3]  
Here's a more detailed explanation: 
Factors contributing to worse air quality in North India: [1, 2, 4, 5, 6]  

• Higher Population Density: North India, particularly the Indo-Gangetic plain, has a much higher population density than the south, leading to increased vehicular traffic, construction, and waste generation, all significant sources of air pollution. [1, 1, 2, 2, 4, 4, 5, 6]  
• Stubble Burning: In the fall, farmers in North India commonly burn crop residue after harvesting rice and before planting wheat. This practice, coupled with the region's geography and weather patterns, can trap pollutants and significantly worsen air quality. [1, 1, 3, 3, 7, 7]  
• Industrial Activity: While South India also has industrial areas, the scale of industrial activity and the associated emissions are often higher in North India. [1, 1, 4, 4, 6]  
• Geography and Weather: The northern plains are largely landlocked, with limited wind movement to disperse pollutants. In contrast, coastal areas in South India benefit from sea breezes that help to clear the air. [2, 2, 4, 4]  
• Diwali Celebrations: Diwali, the festival of lights, is celebrated with firecrackers, which exacerbate air pollution, particularly in North India, where the celebrations are often more intense and prolonged. [2, 2, 3, 3]  
• Winter Season: The winter season in North India is characterized by colder temperatures and stagnant air, which traps pollutants and leads to a significant increase in AQI. [2, 8, 8, 9]  

In contrast, South India generally benefits from: 

• Coastal Geography: Coastal areas in South India experience more wind, which helps to disperse pollutants. [1, 4]  
• Less Stubble Burning: Crop residue burning is less prevalent in the south due to different agricultural practices and the use of residue for other purposes. [2]  
• Generally Higher Education Levels: Some sources suggest that higher education levels in South India contribute to a greater awareness and adoption of pollution control measures. [5, 6]  

Important Considerations: 

Air quality in both North and South India is a concern. 

While North India generally experiences worse air quality, South Indian cities like Bangalore and Chennai also face significant pollution challenges. [1, 1, 4, 4]  

Air pollution is a complex issue 

with multiple contributing factors, and solutions require a multi-pronged approach. [4, 4, 6, 10, 10, 11]  

AI responses may include mistakes.

[1] https://www.youtube.com/watch?v=XZPOQfvBBU8[2] https://www.quora.com/Why-is-there-so-much-pollution-in-North-India-compared-to-South-India[3] https://www.thehindubusinessline.com/data-stories/data-focus/air-quality-during-diwali-worse-in-north-india-compared-to-south-india/article68859706.ece[4] https://breathesafeair.com/air-pollution-in-india/[5] https://www.quora.com/Why-does-South-India-have-a-much-better-air-quality-than-North-India-Is-South-India-or-South-Indians-more-developed-than-North-Indians[6] https://www.quora.com/Why-are-North-Indian-cities-dirtier-than-South-Indian-cities[7] https://www.vox.com/climate/387135/india-pakistan-air-pollution-delhi-lahore-aqi[8] https://factly.in/aqi-data-clear-difference-in-aqi-levels-between-north-south-indian-cities-observed/[9] https://getuhoo.com/blog/home/how-seasonal-changes-affect-air-quality-index-aqi/[10] https://www.aqi.in/blog/air-pollution-in-the-us-and-india/[11] https://www.downtoearth.org.in/pollution/cse-report-finds-dangerous-increase-in-ozone-pollution-across-urban-india
import streamlit as st
import plotly.express as px

fig = px.line([1, 2, 3], y=[1, 3, 2])

# Create a custom styled div
css = """
<div style='border: 2px solid #4CAF50; border-radius: 10px; padding: 20px; margin-bottom: 20px;'>
"""
close_div = "</div>"

st.markdown(css, unsafe_allow_html=True)
st.plotly_chart(fig)
st.markdown(close_div, unsafe_allow_html=True)
