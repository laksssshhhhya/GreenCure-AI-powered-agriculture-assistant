import streamlit as st
import pandas as pd
from agricultural_util import GreenCureAI
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

class GreenCureManager:
    def __init__(self):
        self.recommendations = []
        self.diagnoses = []
        self.soil_analyses = []
        self.weather_advisories = []
        self.market_analyses = []

    def add_recommendation(self, recommendation_data):
        """Add crop recommendation to history"""
        self.recommendations.append({
            **recommendation_data,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def add_diagnosis(self, diagnosis_data):
        """Add disease diagnosis to history"""
        self.diagnoses.append({
            **diagnosis_data,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def add_soil_analysis(self, soil_data):
        """Add soil analysis to history"""
        self.soil_analyses.append({
            **soil_data,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def add_weather_advisory(self, weather_data):
        """Add weather advisory to history"""
        self.weather_advisories.append({
            **weather_data,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def add_market_analysis(self, market_data):
        """Add market analysis to history"""
        self.market_analyses.append({
            **market_data,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def generate_comprehensive_report(self):
        """Generate comprehensive farm report"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"green_cure_comprehensive_report_{timestamp}.pdf"
            os.makedirs('results', exist_ok=True)
            full_path = os.path.join('results', filename)
            
            c = canvas.Canvas(full_path, pagesize=letter)
            width, height = letter
            y = height - 40
            
            c.setFont("Helvetica-Bold", 16)
            c.drawString(40, y, "Green Cure - Comprehensive Agricultural Report")
            y -= 40
            
            c.setFont("Helvetica", 12)
            c.drawString(40, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            y -= 30
            
            if self.recommendations:
                c.setFont("Helvetica-Bold", 14)
                c.drawString(40, y, "CROP RECOMMENDATIONS")
                y -= 20
                c.setFont("Helvetica", 10)
                
                for i, rec in enumerate(self.recommendations[-3:], 1): 
                    lines = [
                        f"Recommendation {i}:",
                        f"Crop: {rec.get('crop_name', 'N/A')}",
                        f"Season: {rec.get('planting_season', 'N/A')}",
                        f"Expected Yield: {rec.get('expected_yield', 'N/A')}",
                        f"Timestamp: {rec.get('timestamp', 'N/A')}",
                        "-" * 60
                    ]
                    
                    for line in lines:
                        if y < 60:
                            c.showPage()
                            y = height - 40
                        c.drawString(40, y, line)
                        y -= 15
                y -= 10
            
            if self.diagnoses:
                c.setFont("Helvetica-Bold", 14)
                c.drawString(40, y, "DISEASE DIAGNOSES")
                y -= 20
                c.setFont("Helvetica", 10)
                
                for i, diag in enumerate(self.diagnoses[-3:], 1): 
                    lines = [
                        f"Diagnosis {i}:",
                        f"Disease: {diag.get('disease_name', 'N/A')}",
                        f"Severity: {diag.get('severity', 'N/A')}",
                        f"Timestamp: {diag.get('timestamp', 'N/A')}",
                        "-" * 60
                    ]
                    
                    for line in lines:
                        if y < 60:
                            c.showPage()
                            y = height - 40
                        c.drawString(40, y, line)
                        y -= 15
                y -= 10
            
            c.save()
            return full_path
            
        except Exception as e:
            st.error(f"Error generating report: {e}")
            return None

def main():
    st.set_page_config(
        page_title="Green Cure - Agricultural AI Assistant",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    if 'green_cure_manager' not in st.session_state:
        st.session_state.green_cure_manager = GreenCureManager()
    
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #FFDBB6;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f8f0;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E7D2E;
    }
    .stButton > button {
        background-color: #2E7D2E;
        color: white;
        border-radius: 0.5rem;
    }
    .success-box {
        background-color: #2F546B;
        border: 1px solid #c3e6cb;
        border-radius: 0.25rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #383673;
        border: 1px solid #bee5eb;
        border-radius: 0.25rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.title("Green Cure")
    st.sidebar.markdown("*AI-Powered Agricultural Solutions*")
    st.sidebar.markdown("---")
    
    menu_options = [
        "Dashboard",
        "Crop Recommendations", 
        "Disease Diagnosis",
        "Soil Analysis",
        "Weather Advisory",
        "Market Analysis",
        "Farm Analytics",
        "Reports"
    ]
    
    selected_option = st.sidebar.selectbox("Choose Service", menu_options)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("AI Configuration")
    api_keys = ["GROQ1", "GROQ2", "GROQ3", "GROQ4"]
    selected_api = st.sidebar.selectbox("Select AI Model", api_keys)
    
    try:
        ai_assistant = GreenCureAI(selected_api)
        st.sidebar.success(f"AI Model {selected_api} Ready")
    except Exception as e:
        st.sidebar.error(f"Failed to initialize AI: {str(e)[:50]}...")
        st.error("Please check your API keys in the .env file")
        return
    
    if selected_option == "Dashboard":
        display_dashboard()
    elif selected_option == "Crop Recommendations":
        display_crop_recommendations(ai_assistant)
    elif selected_option == "Disease Diagnosis":
        display_disease_diagnosis(ai_assistant)
    elif selected_option == "Soil Analysis":
        display_soil_analysis(ai_assistant)
    elif selected_option == "Weather Advisory":
        display_weather_advisory(ai_assistant)
    elif selected_option == "Market Analysis":
        display_market_analysis(ai_assistant)
    elif selected_option == "Farm Analytics":
        display_farm_analytics()
    elif selected_option == "Reports":
        display_reports()

def display_dashboard():
    st.markdown('<h1 class="main-header">Green Cure Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("Welcome to your AI-powered agricultural assistant")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Active Crops", 
            value="12", 
            delta="2",
            help="Number of crops currently being monitored"
        )
    with col2:
        st.metric(
            label="Health Score", 
            value="85%", 
            delta="5%",
            help="Overall farm health assessment"
        )
    with col3:
        st.metric(
            label="Weather Alerts", 
            value="1", 
            delta="0",
            help="Active weather warnings"
        )
    with col4:
        st.metric(
            label="Recommendations", 
            value=str(len(st.session_state.green_cure_manager.recommendations)), 
            delta="+" + str(len(st.session_state.green_cure_manager.recommendations)),
            help="Total AI recommendations generated"
        )
    
    st.markdown("---")
    
    st.subheader("Quick Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h4>Smart Crop Advisory</h4>
        <p>Get AI-powered crop recommendations based on your soil, climate, and market conditions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
        <h4>Disease Diagnosis</h4>
        <p>Upload crop images or describe symptoms for instant disease identification and treatment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-box">
        <h4>Soil Health</h4>
        <p>Comprehensive soil analysis with personalized improvement recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("Recent Activities")
    
    activities_data = []
    
    if st.session_state.green_cure_manager.recommendations:
        activities_data.append({
            'Date': st.session_state.green_cure_manager.recommendations[-1].get('timestamp', 'N/A'),
            'Activity': 'Crop Recommendation Generated',
            'Status': 'Completed',
            'Type': 'Recommendation'
        })
    
    if st.session_state.green_cure_manager.diagnoses:
        activities_data.append({
            'Date': st.session_state.green_cure_manager.diagnoses[-1].get('timestamp', 'N/A'),
            'Activity': 'Disease Diagnosis Completed',
            'Status': 'Completed',
            'Type': 'Diagnosis'
        })
    
    if st.session_state.green_cure_manager.soil_analyses:
        activities_data.append({
            'Date': st.session_state.green_cure_manager.soil_analyses[-1].get('timestamp', 'N/A'),
            'Activity': 'Soil Analysis Completed',
            'Status': 'Completed',
            'Type': 'Analysis'
        })
    
    if not activities_data:
        activities_data = [
            {
                'Date': 'No activities yet',
                'Activity': 'Start by using any Green Cure service',
                'Status': 'Pending',
                'Type': 'Getting Started'
            }
        ]
    
    activities_df = pd.DataFrame(activities_data)
    st.dataframe(activities_df, use_container_width=True)

def display_crop_recommendations(ai_assistant):
    st.markdown('<h1 class="main-header">Smart Crop Recommendations</h1>', unsafe_allow_html=True)
    st.markdown("Get AI-powered crop recommendations tailored for Indian farming conditions")
    
    with st.form("crop_recommendation_form"):
        st.subheader("Farm Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            location = st.text_input(
                "Location/District", 
                placeholder="e.g., Guna, Madhya Pradesh",
                help="Enter your district and state"
            )
            soil_type = st.selectbox("Soil Type", [
                "Black Soil (Regur)", "Red Soil", "Alluvial Soil", 
                "Laterite Soil", "Desert Soil", "Mountain Soil", 
                "Clay", "Sandy", "Loamy"
            ])
        
        with col2:
            season = st.selectbox("Season", [
                "Kharif (Monsoon)", "Rabi (Winter)", "Zaid (Summer)"
            ])
            farm_size = st.selectbox("Farm Size", [
                "Marginal (< 1 hectare)", 
                "Small (1-2 hectares)", 
                "Semi-medium (2-4 hectares)",
                "Medium (4-10 hectares)", 
                "Large (> 10 hectares)"
            ])
        
        submitted = st.form_submit_button("Get AI Recommendations", type="primary", use_container_width=True)
    
    if submitted:
        if not location:
            st.error("Please enter your location")
            return
            
        with st.spinner("AI is analyzing your farming conditions..."):
            try:
                recommendation = ai_assistant.get_crop_recommendation(
                    location, soil_type, season, farm_size
                )
                
                recommendation_data = {
                    'location': location,
                    'soil_type': soil_type,
                    'season': season,
                    'farm_size': farm_size,
                    'crop_name': recommendation.crop_name,
                    'planting_season': recommendation.planting_season,
                    'expected_yield': recommendation.expected_yield,
                    'market_value': recommendation.market_value,
                    'care_instructions': recommendation.care_instructions
                }
                st.session_state.green_cure_manager.add_recommendation(recommendation_data)
                
                # Display results
                st.success("Recommendations Generated Successfully!")
                
                # Main recommendation display
                st.markdown("---")
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"### Recommended Crop: **{recommendation.crop_name}**")
                    
                    info_col1, info_col2 = st.columns(2)
                    with info_col1:
                        st.info(f"**Best Planting Season:** {recommendation.planting_season}")
                    with info_col2:
                        st.info(f"**Expected Yield:** {recommendation.expected_yield}")
                    
                    st.success(f"**Market Value:** {recommendation.market_value}")
                    
                    st.markdown("### Detailed Care Instructions")
                    for idx, instruction in enumerate(recommendation.care_instructions, 1):
                        st.markdown(f"**{idx}.** {instruction}")
                
                with col2:
                    # Farm summary card
                    st.markdown("### Farm Summary")
                    st.markdown(f"**Location:** {location}")
                    st.markdown(f"**Soil:** {soil_type}")
                    st.markdown(f"**Season:** {season}")
                    st.markdown(f"**Size:** {farm_size}")
                    
                    # Action buttons OUTSIDE form
                    st.markdown("### Actions")
                    
                    # Generate detailed report
                    report_content = f"""
GREEN CURE - CROP RECOMMENDATION REPORT
=====================================

Farm Details:
- Location: {location}
- Soil Type: {soil_type}
- Season: {season}
- Farm Size: {farm_size}
- Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

RECOMMENDATION:
Crop: {recommendation.crop_name}
Planting Season: {recommendation.planting_season}
Expected Yield: {recommendation.expected_yield}
Market Value: {recommendation.market_value}

CARE INSTRUCTIONS:
{chr(10).join([f"{i+1}. {instruction}" for i, instruction in enumerate(recommendation.care_instructions)])}

Generated by Green Cure AI Assistant
                    """
                    
                    st.download_button(
                        "Download Report",
                        data=report_content,
                        file_name=f"crop_recommendation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
            except Exception as e:
                st.error(f"Error generating recommendations: {str(e)}")
                st.info("Try different inputs or check your internet connection")

def display_disease_diagnosis(ai_assistant):
    st.markdown('<h1 class="main-header">Smart Disease Diagnosis</h1>', unsafe_allow_html=True)
    st.markdown("AI-powered crop disease identification and treatment recommendations")
    
    with st.form("disease_diagnosis_form"):
        st.subheader("Disease Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            crop_type = st.selectbox("Crop Type", [
                "Wheat", "Rice", "Cotton", "Sugarcane", "Soybean",
                "Maize", "Bajra", "Jowar", "Potato", "Tomato", 
                "Onion", "Garlic", "Chilli", "Other"
            ])
            region = st.text_input("Region/State", placeholder="e.g., Madhya Pradesh")
        
        with col2:
            symptoms = st.text_area(
                "🔍 Describe Symptoms",
                placeholder="Describe what you observe: yellow spots, wilting, brown patches, insect damage, etc.",
                height=100
            )
        
        # Only form submit button inside form
        submitted = st.form_submit_button("Diagnose Disease", type="primary", use_container_width=True)
    
    # All processing logic OUTSIDE the form
    if submitted:
        if not crop_type or not symptoms:
            st.error("Please fill in all required fields")
            return
            
        with st.spinner("AI is analyzing crop symptoms..."):
            try:
                diagnosis = ai_assistant.diagnose_crop_disease(
                    crop_type, symptoms, region
                )
                
                # Store in session state
                diagnosis_data = {
                    'crop_type': crop_type,
                    'region': region,
                    'symptoms_described': symptoms,
                    'disease_name': diagnosis.disease_name,
                    'severity': diagnosis.severity,
                    'symptoms': diagnosis.symptoms,
                    'treatment': diagnosis.treatment,
                    'prevention': diagnosis.prevention
                }
                st.session_state.green_cure_manager.add_diagnosis(diagnosis_data)
                
                # Display results
                st.success("Disease Diagnosis Complete!")
                
                # Severity indicator
                severity_colors = {
                    "Low": "🟢",
                    "Medium": "🟡", 
                    "High": "🔴"
                }
                
                severity_emoji = severity_colors.get(diagnosis.severity, "🔵")
                
                st.markdown("---")
                st.markdown(f"### Diagnosed Disease: **{diagnosis.disease_name}**")
                st.markdown(f"### {severity_emoji} Severity Level: **{diagnosis.severity}**")
                
                # Main content in columns
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.markdown("#### 🔍 Identified Symptoms")
                    for symptom in diagnosis.symptoms:
                        st.markdown(f"• {symptom}")
                    
                    st.markdown("#### Treatment Recommendations")
                    for idx, treatment in enumerate(diagnosis.treatment, 1):
                        st.markdown(f"**{idx}.** {treatment}")
                
                with col2:
                    st.markdown("#### Prevention Measures")
                    for idx, prevention in enumerate(diagnosis.prevention, 1):
                        st.markdown(f"**{idx}.** {prevention}")
                    
                    # Action section
                    st.markdown("#### Actions")
                    
                    # Generate report
                    diagnosis_report = f"""
GREEN CURE - DISEASE DIAGNOSIS REPORT
===================================

Crop Information:
- Crop Type: {crop_type}
- Region: {region}
- Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Symptoms Described:
{symptoms}

DIAGNOSIS:
Disease: {diagnosis.disease_name}
Severity: {diagnosis.severity}

IDENTIFIED SYMPTOMS:
{chr(10).join([f"• {symptom}" for symptom in diagnosis.symptoms])}

TREATMENT RECOMMENDATIONS:
{chr(10).join([f"{i+1}. {treatment}" for i, treatment in enumerate(diagnosis.treatment)])}

PREVENTION MEASURES:
{chr(10).join([f"{i+1}. {prevention}" for i, prevention in enumerate(diagnosis.prevention)])}

Generated by Green Cure AI Assistant
                    """
                    
                    st.download_button(
                        "Download Diagnosis Report",
                        data=diagnosis_report,
                        file_name=f"disease_diagnosis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
            except Exception as e:
                st.error(f"Error in diagnosis: {str(e)}")
                st.info("Try describing symptoms more clearly or check your connection")

def display_soil_analysis(ai_assistant):
    st.markdown('<h1 class="main-header">Smart Soil Analysis</h1>', unsafe_allow_html=True)
    st.markdown("Comprehensive soil health assessment and improvement recommendations")
    
    with st.form("soil_analysis_form"):
        st.subheader("Soil Test Parameters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ph_level = st.slider("Soil pH Level", 1.0, 14.0, 7.0, 0.1)
            organic_matter = st.selectbox("🍃 Organic Matter Content", [
                "Very Low (< 0.5%)", "Low (0.5-1.0%)", "Medium (1.0-3.0%)", 
                "Good (3.0-5.0%)", "High (> 5.0%)"
            ])
        
        with col2:
            drainage = st.selectbox("Drainage Quality", [
                "Very Poor", "Poor", "Fair", "Good", "Excellent"
            ])
            region = st.text_input("Region/District", placeholder="e.g., Guna, Madhya Pradesh")
        
        # Only form submit button inside form
        submitted = st.form_submit_button("Analyze Soil", type="primary", use_container_width=True)
    
    # Processing logic OUTSIDE the form
    if submitted:
        if not region:
            st.error("Please enter your region")
            return
            
        with st.spinner("AI is analyzing soil conditions..."):
            try:
                analysis = ai_assistant.analyze_soil_conditions(
                    ph_level, organic_matter, drainage, region
                )
                
                # Store in session state
                soil_data = {
                    'region': region,
                    'ph_level_input': ph_level,
                    'organic_matter': organic_matter,
                    'drainage': drainage,
                    'soil_type': analysis.soil_type,
                    'ph_analysis': analysis.ph_level,
                    'nutrient_status': analysis.nutrient_status,
                    'recommendations': analysis.recommendations,
                    'suitable_crops': analysis.suitable_crops
                }
                st.session_state.green_cure_manager.add_soil_analysis(soil_data)
                
                # Display results
                st.success("Soil Analysis Complete!")
                
                # pH level visualization
                fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=ph_level,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "Soil pH Level"},
                    delta={'reference': 7},
                    gauge={
                        'axis': {'range': [None, 14]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 6], 'color': "lightcoral"},
                            {'range': [6, 8], 'color': "lightgreen"},
                            {'range': [8, 14], 'color': "lightcoral"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 7
                        }
                    }
                ))
                
                st.markdown("---")
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Soil parameters summary
                    st.markdown("#### Test Parameters")
                    st.info(f"**pH Level:** {ph_level}")
                    st.info(f"**Organic Matter:** {organic_matter}")
                    st.info(f"**Drainage:** {drainage}")
                
                with col2:
                    st.markdown(f"### Soil Type: **{analysis.soil_type}**")
                    st.markdown(f"**pH Analysis:** {analysis.ph_level}")
                    
                    st.markdown("#### Nutrient Status")
                    for nutrient in analysis.nutrient_status:
                        st.markdown(f"• {nutrient}")
                    
                    st.markdown("#### Improvement Recommendations")
                    for idx, rec in enumerate(analysis.recommendations, 1):
                        st.markdown(f"**{idx}.** {rec}")
                
                # Suitable crops section
                st.markdown("---")
                st.markdown("#### Recommended Crops for Your Soil")
                
                # Display crops in a nice grid
                crops_per_row = 4
                crop_rows = [analysis.suitable_crops[i:i + crops_per_row] 
                           for i in range(0, len(analysis.suitable_crops), crops_per_row)]
                
                for row in crop_rows:
                    cols = st.columns(len(row))
                    for col, crop in zip(cols, row):
                        with col:
                            st.success(f"{crop}")
                
                # Download report
                soil_report = f"""
GREEN CURE - SOIL ANALYSIS REPORT
===============================

Test Parameters:
- pH Level: {ph_level}
- Organic Matter: {organic_matter}
- Drainage: {drainage}
- Region: {region}
- Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ANALYSIS RESULTS:
Soil Type: {analysis.soil_type}
pH Analysis: {analysis.ph_level}

NUTRIENT STATUS:
{chr(10).join([f"• {nutrient}" for nutrient in analysis.nutrient_status])}

IMPROVEMENT RECOMMENDATIONS:
{chr(10).join([f"{i+1}. {rec}" for i, rec in enumerate(analysis.recommendations)])}

SUITABLE CROPS:
{chr(10).join([f"• {crop}" for crop in analysis.suitable_crops])}

Generated by Green Cure AI Assistant
                """
                
                st.download_button(
                    "Download Soil Report",
                    data=soil_report,
                    file_name=f"soil_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error in soil analysis: {str(e)}")
                st.info("Try different parameters or check your connection")

def display_weather_advisory(ai_assistant):
    st.markdown('<h1 class="main-header">Weather-Based Farming Advisory</h1>', unsafe_allow_html=True)
    st.markdown("Get real-time weather-based farming recommendations and alerts")
    
    with st.form("weather_advisory_form"):
        st.subheader("Weather Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            location = st.text_input("Location", placeholder="e.g., Guna, Madhya Pradesh")
            current_weather = st.text_area(
                "Current Weather Conditions",
                placeholder="e.g., Heavy rainfall expected, temperature 25°C, humidity 80%, strong winds",
                height=100
            )
        
        with col2:
            crop_stage = st.selectbox("Current Crop Stage", [
                "Land Preparation", "Sowing/Planting", "Germination", 
                "Vegetative Growth", "Flowering/Pollination", 
                "Fruit Development", "Maturity", "Harvesting"
            ])
        
        # Only form submit button inside form    
        submitted = st.form_submit_button("Get Weather Advisory", type="primary", use_container_width=True)
    
    # Processing logic OUTSIDE the form
    if submitted:
        if not location or not current_weather:
            st.error("Please fill in all required fields")
            return
            
        with st.spinner("AI is generating weather advisory..."):
            try:
                advisory = ai_assistant.get_weather_advisory(
                    location, current_weather, crop_stage
                )
                
                # Store in session state
                weather_data = {
                    'location': location,
                    'current_weather': current_weather,
                    'crop_stage': crop_stage,
                    'conditions': advisory.current_conditions,
                    'farming_impact': advisory.farming_impact,
                    'recommendations': advisory.recommendations,
                    'alerts': advisory.alerts
                }
                st.session_state.green_cure_manager.add_weather_advisory(weather_data)
                
                # Display results
                st.success("Weather Advisory Generated!")
                
                st.markdown("---")
                
                # Current conditions
                st.markdown("### Current Weather Conditions")
                st.info(advisory.current_conditions)
                
                # Farming impact
                st.markdown("### Impact on Farming Activities")
                st.warning(advisory.farming_impact)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### Immediate Recommendations")
                    for idx, rec in enumerate(advisory.recommendations, 1):
                        st.markdown(f"**{idx}.** {rec}")
                
                with col2:
                    st.markdown("### Important Alerts")
                    if advisory.alerts:
                        for alert in advisory.alerts:
                            st.error(f"{alert}")
                    else:
                        st.success("No critical alerts at this time")
                
                # Download report
                weather_report = f"""
GREEN CURE - WEATHER ADVISORY REPORT
==================================

Location: {location}
Crop Stage: {crop_stage}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CURRENT WEATHER:
{current_weather}

WEATHER CONDITIONS ANALYSIS:
{advisory.current_conditions}

FARMING IMPACT:
{advisory.farming_impact}

IMMEDIATE RECOMMENDATIONS:
{chr(10).join([f"{i+1}. {rec}" for i, rec in enumerate(advisory.recommendations)])}

ALERTS:
{chr(10).join([f"• {alert}" for alert in advisory.alerts]) if advisory.alerts else "No critical alerts"}

Generated by Green Cure AI Assistant
                """
                
                st.download_button(
                    "Download Weather Report",
                    data=weather_report,
                    file_name=f"weather_advisory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error generating weather advisory: {str(e)}")
                st.info("Try providing more specific weather details")

def display_market_analysis(ai_assistant):
    # st.title("Market Intelligence & Analysis")
    st.markdown('<h1 class="main-header">Market Intelligence & Analysis</h1>', unsafe_allow_html=True)
    st.markdown("Get market insights, pricing trends, and profit optimization strategies")
    
    with st.form("market_analysis_form"):
        st.subheader("Market Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            crop_type = st.selectbox("Crop Type", [
                "Wheat", "Rice", "Cotton", "Sugarcane", "Soybean",
                "Maize", "Bajra", "Jowar", "Potato", "Tomato", 
                "Onion", "Garlic", "Chilli", "Groundnut", "Other"
            ])
            location = st.text_input("Market Location", placeholder="e.g., Guna Mandi, Madhya Pradesh")
        
        with col2:
            quantity = st.selectbox("Expected Quantity", [
                "Small (< 10 quintals)", "Medium (10-50 quintals)", 
                "Large (50-200 quintals)", "Bulk (> 200 quintals)"
            ])
        
        # Only form submit button inside form
        submitted = st.form_submit_button("Get Market Analysis", type="primary", use_container_width=True)
    
    # Processing logic OUTSIDE the form
    if submitted:
        if not crop_type or not location:
            st.error("Please fill in all required fields")
            return
            
        with st.spinner("AI is analyzing market conditions..."):
            try:
                analysis = ai_assistant.get_market_analysis(
                    crop_type, location, quantity
                )
                
                # Store in session state
                market_data = {
                    'crop_type': crop_type,
                    'location': location,
                    'quantity': quantity,
                    'crop_prices': analysis.crop_prices,
                    'demand_forecast': analysis.demand_forecast,
                    'best_selling_time': analysis.best_selling_time,
                    'market_trends': analysis.market_trends,
                    'profit_tips': analysis.profit_tips
                }
                st.session_state.green_cure_manager.add_market_analysis(market_data)
                
                # Display results
                st.success("Market Analysis Complete!")
                
                st.markdown("---")
                
                # Market overview
                st.markdown(f"### Market Analysis for **{crop_type}**")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### Current Pricing Information")
                    for price_info in analysis.crop_prices:
                        st.info(f"{price_info}")
                    
                    st.markdown("#### Best Selling Time")
                    st.success(f"{analysis.best_selling_time}")
                    
                    st.markdown("#### Market Trends")
                    for trend in analysis.market_trends:
                        st.markdown(f"{trend}")
                
                with col2:
                    st.markdown("#### Demand Forecast")
                    st.warning(f"{analysis.demand_forecast}")
                    
                    st.markdown("#### Profit Optimization Tips")
                    for idx, tip in enumerate(analysis.profit_tips, 1):
                        st.markdown(f"**{idx}.** {tip}")
                
                # Download report
                market_report = f"""
GREEN CURE - MARKET ANALYSIS REPORT
=================================

Crop: {crop_type}
Location: {location}
Quantity: {quantity}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CURRENT PRICING:
{chr(10).join([f"• {price}" for price in analysis.crop_prices])}

DEMAND FORECAST:
{analysis.demand_forecast}

BEST SELLING TIME:
{analysis.best_selling_time}

MARKET TRENDS:
{chr(10).join([f"• {trend}" for trend in analysis.market_trends])}

PROFIT OPTIMIZATION TIPS:
{chr(10).join([f"{i+1}. {tip}" for i, tip in enumerate(analysis.profit_tips)])}

Generated by Green Cure AI Assistant
                """
                
                st.download_button(
                    "Download Market Report",
                    data=market_report,
                    file_name=f"market_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error in market analysis: {str(e)}")
                st.info("Try different crop or location details")

def display_farm_analytics():
    st.markdown('<h1 class="main-header">Farm Analytics & Insights</h1>', unsafe_allow_html=True)
    st.markdown("Comprehensive analytics and performance insights for your agricultural operations")
    
    # Sample data for demonstration
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    crop_yield = [120, 140, 160, 180, 200, 220]
    revenue = [50000, 60000, 70000, 80000, 90000, 100000]
    
    # Performance metrics
    st.subheader("Performance Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Recommendations", len(st.session_state.green_cure_manager.recommendations), "📈")
    with col2:
        st.metric("Disease Diagnoses", len(st.session_state.green_cure_manager.diagnoses), "🔬")
    with col3:
        st.metric("Soil Analyses", len(st.session_state.green_cure_manager.soil_analyses), "🌍")
    with col4:
        st.metric("Weather Advisories", len(st.session_state.green_cure_manager.weather_advisories), "🌤️")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Crop yield chart
        fig1 = px.line(x=months, y=crop_yield, title="Expected Crop Yield Trend (Quintals)")
        fig1.update_traces(line_color='green', line_width=3)
        fig1.update_layout(xaxis_title="Month", yaxis_title="Yield (Quintals)")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Revenue chart
        fig2 = px.bar(x=months, y=revenue, title="Projected Monthly Revenue (₹)")
        fig2.update_traces(marker_color='lightgreen')
        fig2.update_layout(xaxis_title="Month", yaxis_title="Revenue (₹)")
        st.plotly_chart(fig2, use_container_width=True)
    
    # Service usage analytics
    st.subheader("Service Usage Analytics")
    
    usage_data = {
        'Service': ['Crop Recommendations', 'Disease Diagnosis', 'Soil Analysis', 'Weather Advisory', 'Market Analysis'],
        'Usage Count': [
            len(st.session_state.green_cure_manager.recommendations),
            len(st.session_state.green_cure_manager.diagnoses),
            len(st.session_state.green_cure_manager.soil_analyses),
            len(st.session_state.green_cure_manager.weather_advisories),
            len(st.session_state.green_cure_manager.market_analyses)
        ]
    }
    
    usage_df = pd.DataFrame(usage_data)
    
    if sum(usage_data['Usage Count']) > 0:
        fig3 = px.pie(usage_df, values='Usage Count', names='Service', 
                      title="Green Cure Service Usage Distribution")
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("Start using Green Cure services to see analytics here!")
    
    # Detailed metrics table
    st.subheader("Detailed Metrics")
    
    metrics_data = {
        'Metric': ['Total AI Consultations', 'Success Rate', 'Average Response Time', 'User Satisfaction'],
        'Value': [
            sum(usage_data['Usage Count']),
            '95%',
            '2.3 seconds',
            '4.8/5.0'
        ],
        'Status': ['📈 Excellent', '✅ High', '⚡ Fast', '😊 Great']
    }
    
    metrics_df = pd.DataFrame(metrics_data)
    st.dataframe(metrics_df, use_container_width=True)

def display_reports():
    # st.title("Reports & Documentation")
    st.markdown('<h1 class="main-header">Reports & Documentation</h1>', unsafe_allow_html=True)
    st.markdown("Generate and download comprehensive agricultural reports and documentation")
    
    # Report generation options
    col1, col2 = st.columns([2, 1])
    
    with col1:
        report_type = st.selectbox("Select Report Type", [
            "Comprehensive Farm Report",
            "Crop Recommendations Summary", 
            "Disease Diagnosis History",
            "Soil Analysis Summary",
            "Weather Advisory Log",
            "Market Analysis Report"
        ])
        
        date_range = st.date_input(
            "Select Date Range",
            value=[datetime.now().date()],
            help="Select date range for report generation"
        )
    
    with col2:
        st.markdown("### Available Data")
        st.info(f"Recommendations: {len(st.session_state.green_cure_manager.recommendations)}")
        st.info(f"Diagnoses: {len(st.session_state.green_cure_manager.diagnoses)}")
        st.info(f"Soil Analyses: {len(st.session_state.green_cure_manager.soil_analyses)}")
        st.info(f"Weather Advisories: {len(st.session_state.green_cure_manager.weather_advisories)}")
    
    if st.button("Generate Report", type="primary", use_container_width=True):
        if report_type == "Comprehensive Farm Report":
            with st.spinner("Generating comprehensive report..."):
                report_path = st.session_state.green_cure_manager.generate_comprehensive_report()
                if report_path:
                    st.success("Comprehensive report generated successfully!")
                    
                    with open(report_path, "rb") as file:
                        st.download_button(
                            "Download PDF Report",
                            data=file.read(),
                            file_name=os.path.basename(report_path),
                            mime="application/pdf"
                        )
        else:
            # Generate text-based reports for other types
            with st.spinner("Generating report..."):
                report_content = generate_specific_report(report_type)
                
                st.success("Report generated successfully!")
                
                # Display preview
                st.subheader("Report Preview")
                st.text_area("Report Content", report_content, height=400)
                
                # Download option
                st.download_button(
                    "Download Report",
                    data=report_content,
                    file_name=f"{report_type.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )

def generate_specific_report(report_type):
    """Generate specific type of report based on user selection"""
    manager = st.session_state.green_cure_manager
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if report_type == "Crop Recommendations Summary":
        content = f"""
GREEN CURE - CROP RECOMMENDATIONS SUMMARY
=======================================
Generated on: {timestamp}

Total Recommendations: {len(manager.recommendations)}

"""
        for i, rec in enumerate(manager.recommendations, 1):
            content += f"""
Recommendation {i}:
- Crop: {rec.get('crop_name', 'N/A')}
- Location: {rec.get('location', 'N/A')}
- Season: {rec.get('season', 'N/A')}
- Expected Yield: {rec.get('expected_yield', 'N/A')}
- Timestamp: {rec.get('timestamp', 'N/A')}
{'-' * 50}
"""
        
    elif report_type == "Disease Diagnosis History":
        content = f"""
GREEN CURE - DISEASE DIAGNOSIS HISTORY
====================================
Generated on: {timestamp}

Total Diagnoses: {len(manager.diagnoses)}

"""
        for i, diag in enumerate(manager.diagnoses, 1):
            content += f"""
Diagnosis {i}:
- Disease: {diag.get('disease_name', 'N/A')}
- Crop: {diag.get('crop_type', 'N/A')}
- Severity: {diag.get('severity', 'N/A')}
- Region: {diag.get('region', 'N/A')}
- Timestamp: {diag.get('timestamp', 'N/A')}
{'-' * 50}
"""
    
    else:
        content = f"""
GREEN CURE - {report_type.upper()}
{'=' * (len(report_type) + 15)}
Generated on: {timestamp}

This report type is being developed.
Please use the Comprehensive Farm Report for detailed information.

Current Data Summary:
- Crop Recommendations: {len(manager.recommendations)}
- Disease Diagnoses: {len(manager.diagnoses)}
- Soil Analyses: {len(manager.soil_analyses)}
- Weather Advisories: {len(manager.weather_advisories)}
- Market Analyses: {len(manager.market_analyses)}
"""
    
    return content

if __name__ == "__main__":
    main()
