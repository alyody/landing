# LGL Digital Solutions Hub - Landing Page

A professional landing page for LGL Group's digital applications, built with Streamlit. This serves as a central hub for accessing various maritime and corporate management tools.

## Features

- **Professional Design**: Modern UI with gradient backgrounds and hover effects
- **Responsive Layout**: 3x3 grid layout that adapts to mobile devices
- **Clickable Modules**: Interactive buttons that open applications in new tabs
- **Icon-Based Navigation**: Each module features distinctive icons and clear descriptions
- **Direct Access Links**: Backup links for reliable navigation
- **Coming Soon Modules**: Placeholder modules for future development

## Modules

### Active Applications
1. **⚓ PORTS & AGENTS** - Port data and agent information
   - URL: https://lglportsagents.streamlit.app/
2. **🚢 VESSEL & TIME** - Vessel details and voyage tracking
   - URL: https://lgldubaidynamicbot.streamlit.app/
3. **👥 HR EMPLOYEE** - HR policies and employee services
   - URL: https://qoder4.streamlit.app/

### Planned Modules
4. **📊 OPERATIONS** - Operational management tools
5. **💰 FINANCE** - Financial management and reporting
6. **📋 COMPLIANCE** - Regulatory compliance tracking
7. **📈 ANALYTICS** - Business intelligence and insights
8. **🔧 MAINTENANCE** - Asset and maintenance management
9. **📞 SUPPORT** - Customer support and help desk

## Installation

1. Clone or download this repository
2. Navigate to the landing page folder:
   ```bash
   cd "landing page"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud Deployment
1. Upload this folder to GitHub
2. Connect to Streamlit Cloud
3. Deploy from the repository
4. Set the main file as `app.py`
5. The app will be available at your Streamlit Cloud URL

## File Structure
```
landing page/
├── app.py                  # Main application file
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Clickable Functionality

The landing page includes two methods for accessing applications:

1. **Primary Method**: Interactive module buttons with click handlers
2. **Backup Method**: Direct access links at the bottom of the page

This ensures reliable navigation regardless of browser restrictions.

## Customization

### Adding New Modules
To add or modify modules, edit the `modules` list in `app.py`:

```python
{
    "icon": "🔧",
    "title": "MODULE NAME",
    "subtitle": "MODULE SUBTITLE",
    "description": "Module description text",
    "url": "https://your-streamlit-app.streamlit.app/",
    "available": True  # Set to False for coming soon modules
}
```

### Updating URLs
Replace the placeholder URLs in the modules list with your actual Streamlit application URLs.

### Styling
Modify the CSS in the `st.markdown()` section to customize colors, fonts, and layout.

## Technical Details

- **Framework**: Streamlit
- **Styling**: Custom CSS with responsive design
- **Layout**: CSS Grid for module arrangement
- **Navigation**: Multiple click handling methods
- **Icons**: Unicode emoji icons (easily replaceable)
- **Theme**: Professional blue gradient with modern shadows

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Deployment Instructions

### For Streamlit Cloud:
1. Create a GitHub repository
2. Upload the entire "landing page" folder
3. Connect to Streamlit Cloud
4. Deploy with `app.py` as the main file

### For Local Testing:
1. Open terminal in the "landing page" folder
2. Run: `streamlit run app.py`
3. Access via: http://localhost:8501

## Support

For technical support or questions about this landing page, contact the development team.

## License

© 2025 LGL Group. All rights reserved.