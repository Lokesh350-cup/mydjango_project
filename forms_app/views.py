# forms_app/views.py
from django.shortcuts import render
from .forms import ForName
from .models import Feedback

def form_name_views(request):
    form = ForName()
    profile_pic_url = None

    if request.method == 'POST':
        form = ForName(request.POST,request.FILES)
        if form.is_valid():
            # Extract cleaned data from the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            profile_pic = form.cleaned_data.get('profile_pic')

            # Save data to the database
            feedback_instance = Feedback.objects.create(
                name=name,
                email=email,
                feedback=feedback,
                profile_pic=profile_pic
            )


            if profile_pic:
                profile_pic_url = feedback_instance.profile_pic.url

            # Print formatted output in the terminal
            print("/n" + "=" * 50)
            print("User Form Submission".center(30))
            print("=" * 50)
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Feedback: {feedback}")
            if profile_pic:
                print(f"profile picture: {profile_pic_url}")
            print("=" * 50 + "\n")

            #Iterate and print each field on a new line
            for field, value in form.cleaned_data.items():
                print(f"{field.capitalize()}: {value}")

                # print bottom line
                print("=" * 50 + "\n")
                print()
    return render(request, 'forms_app/form_page.html', {'form': form, 'profile_pic_url': profile_pic_url})