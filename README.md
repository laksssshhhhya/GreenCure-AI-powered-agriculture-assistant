# 🌱 Green Cure

**AI-Powered Agricultural Solutions**

Green Cure is an AI-powered agricultural decision-support system designed to assist farmers, researchers, and policymakers in making informed agricultural decisions. It integrates **real-time insights, intelligent recommendations, and automated reporting** to address the challenges faced by modern Indian farmers.

The project leverages **Streamlit** for an interactive user interface, **Python** for backend logic, **LangChain** for AI orchestration, and **Gemini-LLaMA-3.1B model (via Groq Cloud API)** for natural language processing and decision-making capabilities.

---

## 🎯 Problem Statement

Indian farmers often face multiple challenges such as:

- Lack of **personalized crop recommendations** based on soil and seasonal conditions.
- Difficulty in identifying **crop diseases** and finding accurate treatment solutions.
- Limited access to **real-time weather advisories** affecting sowing, irrigation, and harvesting decisions.
- Lack of **comprehensive farm documentation and reports** that integrate different insights (soil, weather, diseases, recommendations).
- Over-reliance on guesswork, leading to crop failures, reduced yields, and financial losses.

Green Cure solves these problems by providing an **AI-powered agricultural assistant** that combines **soil, crop, weather, and disease data** into actionable insights.

---

## 🚀 Key Features

### 1. 📊 Reports & Documentation

- Generate **comprehensive agricultural reports** within seconds.
- Allows users to select a report type and a date range.
- Aggregates data from multiple modules (recommendations, diagnoses, soil analyses, weather advisories).
- Provides farmers and stakeholders with **one-click documentation** for analysis and decision-making.
- Useful for agricultural extension officers and researchers who need **data-driven reporting**.

---

### 2. 🌦️ Weather-Based Farming Advisory

- Provides **real-time weather-based farming alerts and recommendations**.
- Takes into account **location, crop stage, and current weather conditions**.
- Advises on actions like irrigation scheduling, pest control, fertilizer application, and harvest timing.
- Helps farmers **mitigate risks due to rainfall variability, temperature fluctuations, or extreme weather events**.
- Example: If heavy rainfall is expected, the advisory may recommend **delaying sowing or improving drainage**.

---

### 3. 🌍 Smart Soil Analysis

- Provides **in-depth soil health assessment** with AI-driven improvement recommendations.
- Parameters analyzed:
  - Soil **pH level** (1–14)
  - **Organic matter content** (low, medium, high)
  - **Drainage quality** (poor, moderate, good)
  - **Region/District** context
- Recommendations include **soil amendments, fertilizers, crop suitability, and sustainable practices**.
- Example: If soil pH is too acidic and organic matter is low, the system may recommend **lime application and composting**.

---

### 4. 🌿 Smart Disease Diagnosis

- AI-powered module for **crop disease detection and treatment recommendations**.
- Farmers input:
  - Crop type (e.g., Wheat, Rice, Maize)
  - Region/State
  - Observed symptoms (yellow spots, wilting, insect damage, fungal patches, etc.)
- Output:
  - Likely **disease identification**.
  - Recommended **treatments and preventive measures**.
- This reduces reliance on guesswork and prevents misdiagnosis.
- Example: For wheat showing **yellow rust symptoms**, the system suggests fungicides and resistant crop varieties.

---

### 5. 🌾 Smart Crop Recommendations

- Suggests **optimal crops for cultivation** based on environmental and farm-specific factors.
- Inputs required:
  - Location/District
  - Soil type (e.g., Black soil, Sandy, Loamy, Alluvial)
  - Season (Kharif, Rabi, Zaid)
  - Farm size (marginal, small, medium, large)
- Recommendations are tailored to **maximize yield, improve soil health, and match local market demand**.
- Example: In black soil during **Kharif season**, the system may recommend **cotton, soybean, or maize**.

---

## 🏗️ System Architecture

1. **Frontend (User Interaction)**

   - Built with **Streamlit**.
   - Provides interactive forms for inputs and easy-to-understand outputs.
   - Modules are presented as separate services for clarity (Reports, Weather Advisory, Soil Analysis, Disease Diagnosis, Crop Recommendations).

2. **Backend (Processing & AI)**

   - Developed in **Python** with structured modules for each service.
   - AI reasoning and responses handled using **LangChain** for chaining multiple queries and contexts.

3. **AI & Model**

   - Uses **Gemini-LLaMA-3.1B** model hosted on **Groq Cloud**.
   - Model used for **NLP, decision-making, and knowledge integration**.
   - Optimized for **agriculture-related context understanding**.

4. **Integration & Deployment**
   - API calls to Groq Cloud for inference.
   - Deployed as a **Streamlit app** for direct accessibility.
   - Modular design allows easy **future expansion** (e.g., pest prediction, market price analysis).

---

## 📌 Example Use Cases

- **Use Case 1: Crop Selection**  
  A farmer in Madhya Pradesh with **black soil** wants to know which crops are best suited for **Kharif season**.  
  → Green Cure suggests **soybean, cotton, and maize** with reasoning.

- **Use Case 2: Disease Identification**  
  A farmer notices **brown patches and wilting on wheat leaves**.  
  → Green Cure identifies the disease (e.g., fungal infection) and provides treatment steps.

- **Use Case 3: Weather Advisory**  
  A farmer is preparing land for sowing, and **heavy rainfall** is predicted in the region.  
  → Green Cure advises **delaying sowing** and preparing **proper drainage systems**.

- **Use Case 4: Soil Improvement**  
  Soil test shows **pH 5.0 (acidic), very low organic content, and poor drainage**.  
  → Green Cure recommends **lime treatment, compost addition, and raised-bed planting**.

- **Use Case 5: Reports for Research**  
  An agricultural officer wants a **report of soil, weather, and crop advisories** for a given timeframe.  
  → Green Cure generates a **comprehensive PDF/structured report** with all insights.

---

## 🏗️ Tech Stack

- **Frontend & UI**: [Streamlit](https://streamlit.io/)
- **Backend Logic**: Python
- **AI Orchestration**: [LangChain](https://www.langchain.com/)
- **AI Model**: Gemini-LLaMA-3.1B (via Groq Cloud API)
- **Deployment**: Streamlit Application

---

## ✅ Current AI Configuration

- **AI Model in Use**: `GROQ1 (Gemini-LLaMA-3.1B)`
- **Status**: Ready and integrated successfully.

---

## 🌟 Vision

The ultimate vision of **Green Cure** is to **empower Indian farmers with AI-driven, low-cost, and highly accessible agricultural intelligence**. By combining soil science, crop management, weather forecasting, and disease detection into one platform, Green Cure reduces risks, improves yields, and supports sustainable farming practices.

This project demonstrates how **AI can revolutionize agriculture**, especially for small and marginal farmers, by providing **data-driven decisions at the right time**.

---

## 👥 Target Users

Green Cure is designed primarily for **agricultural experts and stakeholders** rather than direct farmer use, since it requires inputs like soil pH, organic matter, and disease symptoms, which are often technical and not farmer-friendly.

### 🎯 Direct Users

- **Agricultural Extension Officers**  
  Use the system to generate localized advisories and reports, then share simplified guidance with farmers.

- **Researchers & Scientists**  
  Leverage integrated soil, crop, and weather data for analysis, trials, and studies.

- **Policy Makers & Government Agencies**  
  Utilize aggregated insights to design better agricultural schemes, crop insurance programs, and sustainability initiatives.

- **Agri-Businesses & NGOs**  
  Apply the platform for farmer-support services, advisory programs, and supply chain planning.

### 🌱 Indirect Users (Beneficiaries)

- **Farmers (Small, Marginal, and Commercial)**  
  While they may not interact with the platform directly, farmers benefit through improved crop choices, better disease management, weather-based advisories, and sustainable soil practices provided by extension officers and organizations.

---

## 📌 Use Cases

1. **Crop Selection & Planning**  
   Officers or agri-business agents suggest optimal crops to farmers based on soil, region, and season.

2. **Disease Identification & Treatment**  
   Researchers or extension officers input crop symptoms or test data → system outputs likely disease and treatments → officers explain solutions to farmers.

3. **Weather Advisory**  
   Generate localized weather-based recommendations (irrigation, sowing, harvesting), shared with farmer groups in simple language.

4. **Soil Health Management**  
   Use soil test data or health cards to generate recommendations for soil amendments and sustainable practices.

5. **Comprehensive Reports**  
   Agricultural officers and policymakers create structured reports for monitoring, planning, and decision-making.

---

## 🌟 Advantages

- **Data-Driven Agriculture** → Moves decisions away from guesswork.
- **Empowers Experts** → Gives officers and researchers AI tools for quick and accurate advisories.
- **Indirect Farmer Support** → Farmers receive more reliable, localized, and actionable guidance.
- **Sustainability** → Encourages soil health management and eco-friendly practices.
- **Scalable & Modular** → Can integrate future modules like pest prediction, market price analysis, or irrigation planning.
- **Time-Saving Reports** → Automated, one-click documentation for analysis and policy support.

---

## 🧭 Positioning

Green Cure is **not a farmer-facing app** but a **decision-support system for agricultural experts**.

- **Farmers = Indirect beneficiaries.**
- **Experts (officers, researchers, policymakers, NGOs) = Direct users who interpret and deliver advice.**
