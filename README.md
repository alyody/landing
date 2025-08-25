# LGL Digital Solutions Hub

A professional landing page for LGL Group's digital applications, built with Streamlit. This serves as a central hub for accessing various maritime and corporate management tools.

## Features

- **Professional Design**: Modern UI with gradient backgrounds and hover effects
- **Responsive Layout**: 3x3 grid layout that adapts to mobile devices
- **Icon-Based Navigation**: Each module features distinctive icons and clear descriptions
- **Clickable Modules**: Direct links to live applications
- **Coming Soon Modules**: Placeholder modules for future development

## Modules

### Active Applications
1. **PORTS & AGENTS** - Port data and agent information
2. **VESSEL & TIME** - Vessel details and voyage tracking
3. **HR EMPLOYEE** - HR policies and employee services

### Planned Modules
4. **OPERATIONS** - Operational management tools
5. **FINANCE** - Financial management and reporting
6. **COMPLIANCE** - Regulatory compliance tracking
7. **ANALYTICS** - Business intelligence and insights
8. **MAINTENANCE** - Asset and maintenance management
9. **SUPPORT** - Customer support and help desk

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Local Development
```bash
streamlit run landing_page.py
```

### Streamlit Cloud Deployment
1. Upload this repository to GitHub
2. Connect to Streamlit Cloud
3. Deploy from the repository
4. The app will be available at your Streamlit Cloud URL

## File Structure
```
LGL PROJECT 2025/
├── landing_page.py          # Main application file
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Customization

### Adding New Modules
To add or modify modules, edit the `modules` list in `landing_page.py`:

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
- **Icons**: Unicode emoji icons (easily replaceable)
- **Theme**: Professional blue gradient with modern shadows

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Support

For technical support or questions about this landing page, contact the development team.

## License

© 2025 LGL Group. All rights reserved.