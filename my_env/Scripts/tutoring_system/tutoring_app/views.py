import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import openai

from .forms import SolutionForm

def generate_random_question():
    questions = [
        "Find the derivative of f(x) = sin(x) + cos(x)",
        "Calculate the integral of 2x dx from 0 to 5",
        "Find the limit of (x^2 - 1) / (x - 1) as x approaches 1"
    ]
    return random.choice(questions)

def exercise_view(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST, request.FILES)
        if form.is_valid():
            solution_text = form.cleaned_data['solution_text']
            solution_image = form.cleaned_data['solution_image']

            if solution_image:
                fs = FileSystemStorage()
                filename = fs.save(solution_image.name, solution_image)
                uploaded_file_url = fs.url(filename)

                # Process image using OpenAI API (mock example)
                openai.api_key = 'your-openai-api-key'
                response = openai.Image.create(file=open(uploaded_file_url, "rb"))

                image_text_result = response['choices'][0]['text']
            else:
                image_text_result = "No image uploaded"

            # Process text using OpenAI API
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Solution Text: {solution_text}\nImage Text: {image_text_result}",
                max_tokens=150
            )
            feedback = response.choices[0].text.strip()

            return render(request, 'exercise_app/exercise.html', {
                'form': form,
                'feedback': feedback,
                'question': generate_random_question()
            })
    else:
        form = SolutionForm()

    return render(request, 'exercise_app/exercise.html', {
        'form': form,
        'question': generate_random_question()
    })
