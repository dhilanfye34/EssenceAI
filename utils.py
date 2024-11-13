import openai
import aiohttp
import asyncio
import logging
import os

API_KEY = os.getenv("OPENAI_API_KEY") 
# Set your OpenAI API key from environment variables
openai.api_key = 'sk-proj-rQsYupZksCtjPA1DGXrrT3BlbkFJMzwUpwrDLnJhXrJ7FcQm'

def get_cancer_description(cancer_type):
    # Descriptions for each cancer type
    descriptions = {
        'Breast Cancer': 'Breast cancer is a disease in which cells in the breast grow out of control.',
        'Lung Cancer': 'Lung cancer is a type of cancer that begins in the lungs.',
        'Prostate Cancer': 'Prostate cancer is a cancer in a man\'s prostate, a small walnut-sized gland that produces seminal fluid.',
        'Colorectal Cancer': 'Colorectal cancer is a cancer that starts in the colon or the rectum.',
        'Melanoma (Skin Cancer)': 'Melanoma is a type of skin cancer that develops from the pigment-producing cells known as melanocytes.',
        'Bladder Cancer': 'Bladder cancer is a common type of cancer that begins in the cells of the bladder.',
        'Kidney Cancer': 'Kidney cancer is a type of cancer that starts in the cells of the kidney.',
        'Liver Cancer': 'Liver cancer is a type of cancer that begins in the cells of the liver.',
        'Pancreatic Cancer': 'Pancreatic cancer begins in the tissues of the pancreas.',
        'Thyroid Cancer': 'Thyroid cancer occurs in the cells of the thyroid, a butterfly-shaped gland at the base of your neck.',
        'Leukemia': 'Leukemia is a cancer of the body\'s blood-forming tissues, including the bone marrow and the lymphatic system.',
        'Lymphoma (Hodgkin and Non-Hodgkin)': 'Lymphoma is a cancer of the lymphatic system, which is part of the body\'s germ-fighting network.',
        'Ovarian Cancer': 'Ovarian cancer is a type of cancer that begins in the ovaries.',
        'Endometrial Cancer': 'Endometrial cancer is a type of cancer that begins in the lining of the uterus.',
        'Cervical Cancer': 'Cervical cancer occurs in the cells of the cervix — the lower part of the uterus that connects to the vagina.',
        'Esophageal Cancer': 'Esophageal cancer occurs in the esophagus, a long, hollow tube that runs from your throat to your stomach.',
        'Stomach Cancer': 'Stomach cancer, also known as gastric cancer, is a type of cancer that begins in the stomach.',
        'Brain and Spinal Cord Tumors': 'Brain and spinal cord tumors are masses of abnormal cells in the brain or spinal cord.',
        'Testicular Cancer': 'Testicular cancer occurs in the testicles (testes), which are located inside the scrotum.',
        'Bone Cancer': 'Bone cancer is a rare type of cancer that begins in a bone.',
        'Soft Tissue Sarcoma': 'Soft tissue sarcoma is a type of cancer that begins in the tissues that connect, support, and surround other body structures.',
    }
    return descriptions.get(cancer_type, 'Description not available.')

def get_cancer_facts(cancer_type):
    # Facts for each cancer type
    facts = {
        'Breast Cancer': [
            'Most common cancer among women worldwide.',
            'Early detection can improve survival rates.'
        ],
        'Lung Cancer': [
            'Leading cause of cancer deaths worldwide.',
            'Smoking is the most significant risk factor.'
        ],
        'Prostate Cancer': [
            'Most common cancer in men.',
            'Early detection is key to successful treatment.'
        ],
        'Colorectal Cancer': [
            'Third most common cancer worldwide.',
            'Screening can help detect it early.'
        ],
        'Melanoma (Skin Cancer)': [
            'Most serious type of skin cancer.',
            'Early detection can lead to successful treatment.'
        ],
        'Bladder Cancer': [
            'More common in men than women.',
            'Smoking is a significant risk factor.'
        ],
        'Kidney Cancer': [
            'More common in older adults.',
            'Smoking and obesity are risk factors.'
        ],
        'Liver Cancer': [
            'Often diagnosed at a late stage.',
            'Chronic liver disease is a risk factor.'
        ],
        'Pancreatic Cancer': [
            'Often diagnosed at a late stage.',
            'Smoking and obesity are risk factors.'
        ],
        'Thyroid Cancer': [
            'More common in women than men.',
            'Usually diagnosed at a younger age.'
        ],
        'Leukemia': [
            'Affects blood and bone marrow.',
            'Can occur in both children and adults.'
        ],
        'Lymphoma (Hodgkin and Non-Hodgkin)': [
            'Affects the lymphatic system.',
            'Can occur at any age.'
        ],
        'Ovarian Cancer': [
            'Often diagnosed at a late stage.',
            'Family history is a risk factor.'
        ],
        'Endometrial Cancer': [
            'Most common cancer of the female reproductive organs.',
            'Obesity is a significant risk factor.'
        ],
        'Cervical Cancer': [
            'Caused by persistent infection with certain types of HPV.',
            'Screening can help detect it early.'
        ],
        'Esophageal Cancer': [
            'More common in men than women.',
            'Smoking and heavy alcohol use are risk factors.'
        ],
        'Stomach Cancer': [
            'More common in older adults.',
            'Diet and smoking are risk factors.'
        ],
        'Brain and Spinal Cord Tumors': [
            'Can occur at any age.',
            'Symptoms depend on the tumor location.'
        ],
        'Testicular Cancer': [
            'Most common cancer in young men.',
            'Highly treatable, especially when detected early.'
        ],
        'Bone Cancer': [
            'Rare type of cancer.',
            'Can occur in any bone.'
        ],
        'Soft Tissue Sarcoma': [
            'Can occur in any part of the body.',
            'More than 50 different types exist.'
        ],
    }
    return facts.get(cancer_type, [])

async def summarize_article_title(title):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following article title briefly and clearly: {title}"}
        ],
        "max_tokens": 50,
        "n": 1,
        "temperature": 0.7,
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                response_data = await response.json()
                logging.info(f"API Response: {response_data}")  # Log the full response for debugging

                # Check if 'choices' is in the response data
                if 'choices' in response_data:
                    summary = response_data["choices"][0]["message"]["content"].strip()
                    logging.info(f"Title summary: {summary}")
                    return summary
                else:
                    # Log and handle cases where 'choices' is missing
                    logging.error(f"'choices' not found in response: {response_data}")
                    return "Summary not available"
    except Exception as e:
        logging.error(f"Error summarizing article title: {e}")
        return "Summary not available"
    
"""
def summarize_article(content):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": (
                    f"Summarize the following article in a detailed and lengthy manner, "
                    f"but ensure it is easily understandable for someone without a medical background. "
                    f"Simplify and explain all key ideas, medical terminology, and concepts to enhance comprehension: {content}"
                )}
            ],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error summarizing article: {e}")
        return "Summary not available"
"""