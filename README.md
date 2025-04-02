# PixelTracker - Habit Tracking System

## 🎯 Project Description  
Automated habit tracking solution using Pixela API to visualize progress through customizable graphs with daily activity logging.

## 📦 Deliverables  
- Python script for pixel-based habit tracking  
- Automatic user/graph creation system  
- API integration with error handling  
- Environment variables configuration  

## 🚀 Key Features  
- 📊 Automatic graph initialization  
- 📅 Daily activity tracking with datetime  
- 🔄 Idempotent operations (prevents duplicate resources)  
- 🔐 Secure token-based authentication  

## 🛠️ Technologies Used  
| Component              | Technology                          |
|------------------------|-------------------------------------|
| **Language**           | Python 3                            |
| **API Service**        | Pixela (https://pixe.la)            |
| **Env Management**     | python-dotenv                       |
| **Date Handling**      | datetime                            |

## ⚙️ Installation & Setup  

### 1. Clone Repository  
```bash
git clone https://github.com/My-Py-Projects/pixel-tracker.git
cd pixel-tracker
```

### 2. Install Dependencies  
```bash
pip install requests python-dotenv
```

### 3. Environment Configuration  
Create a .env file in root directory with:

```ini
# Pixela Configuration
USER_TOKEN=your_secret_token_here
USER_NAME=your_username
GRAPH_ID=habit-tracker
```

### 4. Run Application  
```bash
python main.py
```

### 5. Check Your Graph  
```
https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}.html
```

**Important Notes:**  
```plaintext
1. Required API Documentation:
   - Pixela: https://docs.pixe.la

2. Data Management:
   - To update/delete entries or access advanced features, consult:
   - Official API documentation: https://docs.pixe.la
```