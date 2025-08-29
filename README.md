# Master Challenge

![image](https://github.com/HKIBIMTechnical/HKIBIM-BIMAutomationArena-2025-Master-Challenge-Andy/blob/main/image/image.png)

## Overview
This project is a Streamlit-based web application for the HKIBIM BIM Automation Arena 2025 Master Challenge. It demonstrates advanced BIM automation workflows, multi-software integration, and AI-powered features for the AEC industry. The app showcases parametric modeling, automation scripts, and interactive 3D visualization, integrating tools such as Digital Project, Rhino, Grasshopper, Tekla, Navisworks, Matlab, and more.

## Features
- **Multi-software Integration:** Automates workflows across Digital Project, Rhino, Grasshopper, Tekla, Navisworks, Matlab, and others.
- **Parametric Modeling:** Interactive parameter adjustment and geometry generation.
- **Panel and Point Generation:** Automated extraction and manipulation of geometry from BIM models.
- **3D Visualization:** Embedded 3D model viewers (via Speckle) and video demonstrations.
- **AI Assistant:** Integrates with AI models (Grok, Deepseek, GPT-4o-mini, etc.) for BIM data analysis and chat.
- **Demo Pages:**
  - **Demo1:** Wireframe extraction, curve smoothing, point and panel generation from Rhino models.
  - **Demo2:** Parametric shell and panel automation, with code and video walkthroughs.
  - **Demo3:** Combined workflows and 3D results, with interactive Speckle viewers.
  - **Summary:** Project summary, video, and links to related resources.

## Installation
1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd Automation-2025-Master-Challenge
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   **Required packages:**
   - streamlit
   - pywin32
   - pyxll
   - streamlit-flow-component
   - plotly
   - matlabengine==24.2.2
   - pandasai>=3.0.0b5
   - pandasai-openai

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser to the provided local URL.
3. Use the sidebar to navigate between the Master Challenge question, demos, and summary pages.

## Project Structure
- `app.py` — Main Streamlit app entry point and navigation.
- `pages/` — Contains individual demo and summary pages.
- `adfun.py` — Core automation and utility functions for BIM software integration.
- `image/` — Images and videos for demos and documentation.
- `requirements.txt` — Python dependencies.

## Related Resources
- [HKIBIM_Automation_2025_Demo2_Grasshopper_Plugins](https://github.com/zmq6931/HKIBIM_Automation_2025_Demo2_Grasshopper_Plugins.git)
- [HKIBIM_BIM_Automation_Arena_2025](https://github.com/zmq6931/HKIBIM_BIM_Automation_Arena_2025.git)

## Acknowledgements
- Developed by Andy for the HKIBIM Master Challenge 2025.
- Integrates multiple BIM and AI technologies for advanced automation.
