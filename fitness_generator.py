import google.generativeai as genai

genai.configure(api_key="AIzaSyXXXXXXX")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_plan(goal):

    prompt = f"Create a detailed 7-day workout plan for {goal}"

    response = model.generate_content(prompt)

    return response.text


def generate_diet(goal):

    prompt = f"Create a healthy 7-day diet plan for someone whose goal is {goal}"

    response = model.generate_content(prompt)


    return response.text
