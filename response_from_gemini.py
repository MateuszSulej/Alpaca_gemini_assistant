from google import genai


def response_from_gemini(text):
    client = genai.Client(api_key="AIzaSyBgZZonW8TU-J_3Kb6lT4wx9xD64XQksBo")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=text
    )

    return response.text


def get_data_from_file(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    return data
