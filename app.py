import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LGL Digital Solutions Hub",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin: 0;
        font-weight: 700;
    }
    
    .main-header p {
        color: #e8f4f8;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
    }
    
    .module-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
        text-align: center;
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        cursor: pointer;
    }
    
    .module-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        border-color: #2a5298;
    }
    
    .module-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        color: #2a5298;
    }
    
    .module-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1e3c72;
        margin-bottom: 0.5rem;
    }
    
    .module-subtitle {
        font-size: 1.1rem;
        font-weight: 600;
        color: #4a5568;
        margin-bottom: 1rem;
    }
    
    .module-description {
        font-size: 0.95rem;
        color: #718096;
        line-height: 1.5;
        margin-bottom: 1.5rem;
        flex-grow: 1;
    }
    
    .module-button {
        background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
        color: white !important;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none !important;
        display: inline-block;
        width: 100%;
    }
    
    .module-button:hover {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3);
        color: white !important;
        text-decoration: none !important;
    }
    
    .module-button:visited {
        color: white !important;
        text-decoration: none !important;
    }
    
    .module-button:active {
        color: white !important;
        text-decoration: none !important;
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .coming-soon {
        background: linear-gradient(135deg, #718096 0%, #4a5568 100%);
        cursor: not-allowed;
    }
    
    .coming-soon:hover {
        background: linear-gradient(135deg, #4a5568 0%, #718096 100%);
        transform: none;
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
    }
    
    @media (max-width: 768px) {
        .grid-container {
            grid-template-columns: 1fr;
        }
        .main-header h1 {
            font-size: 2rem;
        }
    }
    
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Hide Streamlit default elements */
    .stButton > button {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="main-header">
    <h1>🚢 LGL Digital Solutions Hub</h1>
    <p>Your Gateway to Maritime & Corporate Excellence</p>
</div>
""", unsafe_allow_html=True)

# Module data
modules = [
    {
        "icon": "⚓",
        "title": "PORTS & AGENTS",
        "subtitle": "PORT DATA AND AGENTS",
        "description": "Query Port Data, free time at different ports, Agent details, Port conditional data and review and special instructions for the specified port",
        "url": "https://lglportsagents.streamlit.app/",
        "available": True
    },
    {
        "icon": "🚢",
        "title": "VESSEL & TIME",
        "subtitle": "VESSEL AND THEIR DETAILS",
        "description": "Review each voyage and the port calls under that voyage. Gets the latest up to date information at your fingertips. Sample data for your review",
        "url": "https://lgldubaidynamicbot.streamlit.app/",
        "available": True
    },
    {
        "icon": "👥",
        "title": "HR EMPLOYEE",
        "subtitle": "HR AND EMPLOYEE SERVICES",
        "description": "From checking the latest in HR policies to requesting for any company or personal related matters",
        "url": "https://qoder4.streamlit.app/",
        "available": True
    },
    {
        "icon": "📊",
        "title": "OPERATIONS",
        "subtitle": "OPERATIONAL MANAGEMENT",
        "description": "Streamline daily operations, track performance metrics, and manage operational workflows with comprehensive tools and analytics",
        "url": "#",
        "available": False
    },
    {
        "icon": "💰",
        "title": "FINANCE",
        "subtitle": "FINANCIAL MANAGEMENT",
        "description": "Access financial reports, budget tracking, expense management, and comprehensive financial analytics for informed decision making",
        "url": "#",
        "available": False
    },
    {
        "icon": "📋",
        "title": "COMPLIANCE",
        "subtitle": "REGULATORY COMPLIANCE",
        "description": "Monitor compliance requirements, regulatory updates, audit trails, and ensure adherence to maritime and corporate standards",
        "url": "#",
        "available": False
    },
    {
        "icon": "📈",
        "title": "ANALYTICS",
        "subtitle": "BUSINESS INTELLIGENCE",
        "description": "Generate insights from data analytics, performance dashboards, KPI tracking, and strategic business intelligence reports",
        "url": "#",
        "available": False
    },
    {
        "icon": "🔧",
        "title": "MAINTENANCE",
        "subtitle": "ASSET MANAGEMENT",
        "description": "Track vessel maintenance schedules, equipment status, repair histories, and optimize maintenance operations efficiently",
        "url": "#",
        "available": False
    },
    {
        "icon": "📞",
        "title": "SUPPORT",
        "subtitle": "CUSTOMER SUPPORT",
        "description": "Access help desk, technical support, documentation, training materials, and customer service resources",
        "url": "#",
        "available": False
    }
]

# Create grid layout with clickable buttons
cols = st.columns(3)

for i, module in enumerate(modules):
    col_index = i % 3
    
    with cols[col_index]:
        # Create unique key for each button
        button_key = f"module_{i}_{module['title'].replace(' ', '_').lower()}"
        
        # Create module container with proper button
        if module["available"]:
            # Create a clickable button that opens URL
            if st.button(
                f"{module['icon']}\n\n**{module['title']}**\n\n{module['subtitle']}\n\n{module['description']}\n\n🚀 Launch Application",
                key=button_key,
                help=f"Click to open {module['title']}"
            ):
                st.write(f"🚀 Opening {module['title']}...")
                st.markdown(f'<meta http-equiv="refresh" content="0; url={module["url"]}">', unsafe_allow_html=True)
                # Alternative method using JavaScript
                st.markdown(f"""
                <script>
                window.open('{module["url"]}', '_blank');
                </script>
                """, unsafe_allow_html=True)
        else:
            # Coming soon button
            if st.button(
                f"{module['icon']}\n\n**{module['title']}**\n\n{module['subtitle']}\n\n{module['description']}\n\n⏳ Coming Soon",
                key=button_key,
                help="This module is coming soon",
                disabled=True
            ):
                st.info("This module is coming soon!")

# Add direct link buttons as backup
st.markdown("---")
st.markdown("### 🔗 Direct Access Links")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Open Ports & Agents", key="direct_ports"):
        st.markdown('<a href="https://lglportsagents.streamlit.app/" target="_blank">Click here if redirect fails</a>', unsafe_allow_html=True)

with col2:
    if st.button("🚀 Open Vessel & Time", key="direct_vessel"):
        st.markdown('<a href="https://lgldubaidynamicbot.streamlit.app/" target="_blank">Click here if redirect fails</a>', unsafe_allow_html=True)

with col3:
    if st.button("🚀 Open HR Employee", key="direct_hr"):
        st.markdown('<a href="https://qoder4.streamlit.app/" target="_blank">Click here if redirect fails</a>', unsafe_allow_html=True)

# Footer
st.markdown("""
---
<div style="text-align: center; padding: 2rem; color: #718096;">
    <p><strong>LGL Digital Solutions Hub</strong> | Powered by Streamlit | © 2025 LGL Group</p>
    <p>Transforming Maritime Operations Through Digital Innovation</p>
</div>
""", unsafe_allow_html=True)