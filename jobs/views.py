import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from common.utils.email import send_email
from .models import Applicant 
from .forms import JobApplicationForm


DAY_NAMES = {
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
}


class JobAppView(CreateView):
    model = Applicant
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

    def form_valid(self, form):
        data = form.cleaned_data.copy()
        
        # Extract form-only fields before saving model
        available_days = data.pop('available_days', [])
        confirmation = data.pop('confirmation', False)
        
        # Send the email
        to = 'josephfacio@comcast.net'  # Recommend using settings.DEFAULT_FROM_EMAIL
        subject = 'Application for Joke Writer'
        content = '<p>Hey HR Manager!</p><p>Job application received:</p><ol>'

        for key, value in data.items():
            label = key.replace('_', ' ').title()

            if isinstance(value, bool):
                entry = 'Yes' if value else 'No'
            else:
                entry = html.escape(str(value), quote=False)

            content += f'<li><strong>{label}</strong>: {entry}</li>'

        if available_days:
            readable_days = ', '.join(DAY_NAMES.get(day, str(day)) for day in available_days)
            content += f'<li><strong>Available Days</strong>: {readable_days}</li>'

        content += f'<li><strong>Confirmation</strong>: {"Yes" if confirmation else "No"}</li>'
        content += '</ol>'

        send_email(to, subject, content)

        return super().form_valid(form)


class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'
