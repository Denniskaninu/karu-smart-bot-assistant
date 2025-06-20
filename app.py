from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime
import dotenv
app = Flask(__name__)
CORS(app)

# Configure Gemini API
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not found in environment variables")
model = genai.GenerativeModel('gemini-pro')

class KaruBot:
    def __init__(self):
        self.university_data = self.load_karu_knowledge_base()
        
    def load_karu_knowledge_base(self):
        """Comprehensive knowledge base about Karatina University"""
        return {
            "general_info": {
                "name": "Karatina University",
                "location": "Karatina, Nyeri County, Kenya",
                "established": "2007",
                "type": "Public University",
                "motto": "Advancing Knowledge for Humanity",
                "website": "https://www.karu.ac.ke/",
                "email": "info@karu.ac.ke",
                "phone": "+254-061-2031000",
                "postal_address": "P.O. Box 1814-10101, Karatina, Kenya"
            },
            "academics": {
                "schools": [
                    {
                        "name": "School of Agriculture and Biotechnology",
                        "programs": [
                            "Bachelor of Science in Agriculture",
                            "Bachelor of Science in Horticulture",
                            "Bachelor of Science in Agricultural Economics and Resource Management",
                            "Bachelor of Science in Food Science and Technology",
                            "Bachelor of Science in Biotechnology"
                        ]
                    },
                    {
                        "name": "School of Business",
                        "programs": [
                            "Bachelor of Commerce",
                            "Bachelor of Business Administration",
                            "Bachelor of Science in Economics",
                            "Bachelor of Cooperative Management"
                        ]
                    },
                    {
                        "name": "School of Education and Social Sciences",
                        "programs": [
                            "Bachelor of Education Arts",
                            "Bachelor of Education Science",
                            "Bachelor of Arts in Social Work",
                            "Bachelor of Arts in Psychology",
                            "Bachelor of Arts in Criminology and Security Studies"
                        ]
                    },
                    {
                        "name": "School of Natural Resources",
                        "programs": [
                            "Bachelor of Science in Environmental Science",
                            "Bachelor of Science in Natural Resource Management",
                            "Bachelor of Science in Water Resource Management"
                        ]
                    },
                    {
                        "name": "School of Pure and Applied Sciences",
                        "programs": [
                            "Bachelor of Science in Computer Science",
                            "Bachelor of Science in Information Technology",
                            "Bachelor of Science in Mathematics",
                            "Bachelor of Science in Statistics",
                            "Bachelor of Science in Chemistry",
                            "Bachelor of Science in Physics"
                        ]
                    }
                ]
            },
            "admissions": {
                "requirements": {
                    "undergraduate": "KCSE mean grade of C+ and above",
                    "diploma": "KCSE mean grade of C- and above",
                    "certificate": "KCSE mean grade of D+ and above"
                },
                "application_process": [
                    "Visit KUCCPS portal for undergraduate programs",
                    "Submit online application with required documents",
                    "Pay application fee",
                    "Await admission letter",
                    "Report to university with required documents"
                ],
                "contacts": {
                    "admission_office": "admissions@karu.ac.ke",
                    "phone": "+254-061-2031000"
                }
            },
            "facilities": [
                "Modern lecture halls and laboratories",
                "Library and information center",
                "Computer laboratories",
                "Student hostels (accommodation)",
                "Cafeteria and dining facilities",
                "Sports and recreation facilities",
                "Health center",
                "Banking services"
            ],
            "student_services": {
                "accommodation": {
                    "description": "On-campus hostels available for students",
                    "contact": "accommodation@karu.ac.ke"
                },
                "library": {
                    "description": "Well-equipped library with digital resources",
                    "contact": "library@karu.ac.ke"
                },
                "health": {
                    "description": "Campus health center for medical services",
                    "contact": "health@karu.ac.ke"
                },
                "counseling": {
                    "description": "Counseling and guidance services",
                    "contact": "counseling@karu.ac.ke"
                }
            },
            "research": {
                "focus_areas": [
                    "Agriculture and Food Security",
                    "Environmental Conservation",
                    "Water Resources Management",
                    "Biotechnology and Innovation",
                    "Rural Development"
                ],
                "contact": "research@karu.ac.ke"
            },
            "quick_links": {
                "student_portal": "https://portal.karu.ac.ke/",
                "e_learning": "https://elearning.karu.ac.ke/",
                "library_portal": "https://library.karu.ac.ke/",
                "kuccps": "https://students.kuccps.net/",
                "helb": "https://www.helb.co.ke/",
                "admission_portal": "https://admissions.karu.ac.ke/"
            },
            "fees": {
                "undergraduate": "Varies by program (approximately KES 16,000 - 25,000 per semester)",
                "diploma": "Varies by program (approximately KES 12,000 - 18,000 per semester)",
                "accommodation": "KES 8,000 - 12,000 per semester",
                "note": "Fees are subject to change. Contact finance office for current rates."
            },
            "contact_departments": {
                "registrar": "registrar@karu.ac.ke",
                "finance": "finance@karu.ac.ke",
                "student_affairs": "studentaffairs@karu.ac.ke",
                "ict": "ict@karu.ac.ke",
                "procurement": "procurement@karu.ac.ke"
            }
        }
    
    def generate_response(self, user_query):
        """Generate intelligent response using Gemini AI with KARU knowledge base"""
        
        # Create context from knowledge base
        context = f"""
        You are KARU Bot, an intelligent virtual assistant for Karatina University (KARU). 
        You have comprehensive knowledge about the university and should provide helpful, accurate information.
        
        UNIVERSITY INFORMATION:
        {self.format_knowledge_base()}
        
        INSTRUCTIONS:
        - Use a friendly, professional tone.
        - Provide specific details from the knowledge base when relevant.
        - Include links or contact info only when necessary.
        - If the query is unclear, respond with a helpful clarification question.
        - Do not repeat generic phrases like 'Thank you for your question' unless appropriate.ents
        
        USER QUERY: {user_query}
        
        Response:
        """
        
        try:
            response = model.generate_content(context)
            return response.text
        except Exception as e:
            return self.get_fallback_response(user_query)
    
    def format_knowledge_base(self):
        """Format knowledge base for context"""
        formatted = ""
        for category, data in self.university_data.items():
            formatted += f"\n{category.upper()}:\n"
            if isinstance(data, dict):
                for key, value in data.items():
                    formatted += f"- {key}: {value}\n"
            elif isinstance(data, list):
                for item in data:
                    formatted += f"- {item}\n"
        return formatted
    
    def get_fallback_response(self, query):
        """Fallback response when AI is unavailable"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['admission', 'apply', 'requirement']):
            return """
            **KARU Admissions Information:**
            
            **Requirements:**
            - Undergraduate: KCSE mean grade of C+ and above
            - Diploma: KCSE mean grade of C- and above
            
            **How to Apply:**
            1. Visit KUCCPS portal: https://students.kuccps.net/
            2. Submit online application
            3. Pay application fee
            4. Await admission letter
            
            **Contact:** admissions@karu.ac.ke | +254-061-2031000
            """
        
        elif any(word in query_lower for word in ['fee', 'cost', 'payment']):
            return """
            **KARU Fee Structure:**
            
            - Undergraduate: KES 16,000 - 25,000 per semester
            - Diploma: KES 12,000 - 18,000 per semester  
            - Accommodation: KES 8,000 - 12,000 per semester
            
            *Fees vary by program and are subject to change*
            
            **Contact:** finance@karu.ac.ke | +254-061-2031000
            """
        
        elif any(word in query_lower for word in ['course', 'program', 'study']):
            return """
            **KARU Academic Programs:**
            
            **Schools:**
            - Agriculture and Biotechnology
            - Business  
            - Education and Social Sciences
            - Natural Resources
            - Pure and Applied Sciences
            
            **Popular Programs:**
            - Computer Science & IT
            - Agriculture & Horticulture
            - Business Administration
            - Education
            - Environmental Science
            
            **More Info:** Visit https://www.karu.ac.ke/ or call +254-061-2031000
            """
        
        return """
        I'm here to help with information about Karatina University! 
        
        **Quick Contacts:**
        - General Info: info@karu.ac.ke
        - Admissions: admissions@karu.ac.ke  
        - Phone: +254-061-2031000
        - Website: https://www.karu.ac.ke/
        
        **Useful Links:**
        - Student Portal: https://portal.karu.ac.ke/
        - E-Learning: https://elearning.karu.ac.ke/
        - KUCCPS: https://students.kuccps.net/
        
        Please ask me anything about admissions, programs, fees, facilities, or campus life!
        """

# Initialize bot
karu_bot = KaruBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'response': 'Please ask me something about Karatina University!',
                'status': 'error'
            })
        
        # Generate response
        bot_response = karu_bot.generate_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'status': 'success',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'response': 'I apologize, but I encountered an error. Please try again or contact info@karu.ac.ke for assistance.',
            'status': 'error'
        })

@app.route('/quick-info/<info_type>')
def quick_info(info_type):
    """Endpoint for quick information queries"""
    try:
        if info_type == 'admissions':
            return jsonify(karu_bot.university_data['admissions'])
        elif info_type == 'programs':
            return jsonify(karu_bot.university_data['academics'])
        elif info_type == 'contacts':
            return jsonify(karu_bot.university_data['contact_departments'])
        elif info_type == 'links':
            return jsonify(karu_bot.university_data['quick_links'])
        else:
            return jsonify({'error': 'Information type not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve information'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)