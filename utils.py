import openai

def get_cancer_description(cancer_type):
    # Placeholder function to return a description for each cancer type
    descriptions = {
        'Breast Cancer': 'Breast cancer is a disease in which cells in the breast grow out of control.',
        # Add descriptions for other cancer types
    }
    return descriptions.get(cancer_type, 'Description not available.')

def get_cancer_facts(cancer_type):
    # Placeholder function to return facts for each cancer type
    facts = {
        'Breast Cancer': [
            'Most common cancer among women worldwide.',
            'Early detection can improve survival rates.'
            # Add more facts
        ],
        # Add facts for other cancer types
    }
    return facts.get(cancer_type, [])

def summarize_article_title(title):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following article title briefly: {title}"}
            ],
            max_tokens=50,  # Keep it brief
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error summarizing article title: {e}")
        return "Summary not available"