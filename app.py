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
        padding: 1.5rem;
        margin: 0.5rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
        text-align: center;
        height: 350px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
    }
    
    .module-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        border-color: #2a5298;
    }
    
    .module-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    
    .module-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        color: #2a5298;
    }
    
    .module-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1e3c72;
        margin-bottom: 0.5rem;
    }
    
    .module-subtitle {
        font-size: 1rem;
        font-weight: 600;
        color: #4a5568;
        margin-bottom: 1rem;
    }
    
    .module-description {
        font-size: 0.9rem;
        color: #718096;
        line-height: 1.4;
        margin-bottom: 1.5rem;
        flex-grow: 1;
    }
    
    .module-button {
        background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
        color: white;
        border: none;
        padding: 12px 20px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: block;
        width: 100%;
        margin-top: auto;
        position: relative;
        z-index: 10;
    }
    
    .module-button:hover {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(30, 60, 114, 0.4);
        color: white;
    }
    
    .module-button.coming-soon {
        background: linear-gradient(135deg, #718096 0%, #4a5568 100%);
        cursor: not-allowed;
        opacity: 0.7;
    }
    
    .module-button.coming-soon:hover {
        background: linear-gradient(135deg, #4a5568 0%, #718096 100%);
        transform: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    @media (max-width: 768px) {
        .grid-container {
            grid-template-columns: 1fr;
        }
        .main-header h1 {
            font-size: 2rem;
        }
        .module-container {
            height: 320px;
        }
    }
    
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Hide Streamlit buttons */
    .element-container .stButton {
        display: none !important;
    }
    
    .backup-links {
        margin-top: 2rem;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .backup-button {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 0.25rem;
    }
    
    .backup-button:hover {
        background: linear-gradient(135deg, #38a169 0%, #48bb78 100%);
        transform: scale(1.05);
        color: white;
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

# Create grid layout with integrated module cards
st.markdown('<div class="grid-container">', unsafe_allow_html=True)

# Initialize cols variable
cols = st.columns(3)

for i, module in enumerate(modules):
    if i % 3 == 0:
        cols = st.columns(3)
    
    col_index = i % 3
    
    with cols[col_index]:
        # Create unique key for each button
        button_key = f"module_{i}_{module['title'].replace(' ', '_').lower()}"
        
        # Create module container with integrated button
        if module["available"]:
            button_class = "module-button"
            button_text = "🚀 Launch Application"
            onclick_action = f"window.open('{module['url']}', '_blank');"
        else:
            button_class = "module-button coming-soon"
            button_text = "⏳ Coming Soon"
            onclick_action = "alert('This module is coming soon!');"
        
        # Render module card with integrated button
        st.markdown(f"""
        <div class="module-container">
            <div class="module-content">
                <div class="module-icon">{module['icon']}</div>
                <div class="module-title">{module['title']}</div>
                <div class="module-subtitle">{module['subtitle']}</div>
                <div class="module-description">{module['description']}</div>
            </div>
            <button class="{button_class}" onclick="{onclick_action}">
                {button_text}
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden Streamlit button for functionality
        if module["available"]:
            if st.button(f"Hidden {module['title']}", key=button_key, help="Hidden button"):
                st.markdown(f"""
                <script>
                window.open('{module['url']}', '_blank');
                </script>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Add direct link buttons as backup
st.markdown("""
<div class="backup-links">
    <h3 style="text-align: center; color: #1e3c72; margin-bottom: 1rem;">🔗 Direct Access Links</h3>
    <div style="text-align: center;">
        <a href="https://lglportsagents.streamlit.app/" target="_blank" class="backup-button">⚓ Ports & Agents</a>
        <a href="https://lgldubaidynamicbot.streamlit.app/" target="_blank" class="backup-button">🚢 Vessel & Time</a>
        <a href="https://qoder4.streamlit.app/" target="_blank" class="backup-button">👥 HR Employee</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer with JavaScript for enhanced functionality
st.markdown("""
---
<div style="text-align: center; padding: 2rem; color: #718096;">
    <p><strong>LGL Digital Solutions Hub</strong> | Powered by Streamlit | © 2025 LGL Group</p>
    <p>Transforming Maritime Operations Through Digital Innovation</p>
</div>

<script>
// Enhanced click handling for module buttons
document.addEventListener('DOMContentLoaded', function() {
    // Add click handlers to all module buttons
    const moduleButtons = document.querySelectorAll('.module-button:not(.coming-soon)');
    moduleButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const onclick = this.getAttribute('onclick');
            if (onclick) {
                eval(onclick);
            }
        });
    });
    
    // Add hover effects
    const moduleContainers = document.querySelectorAll('.module-container');
    moduleContainers.forEach(container => {
        container.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
            this.style.boxShadow = '0 15px 45px rgba(0,0,0,0.2)';
        });
        
        container.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 8px 32px rgba(0,0,0,0.08)';
        });
    });
});

// Fallback function for opening URLs
function openApp(url) {
    window.open(url, '_blank');
}
</script>
""", unsafe_allow_html=True)