from typing import Any
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from subscription.forms import SubscriptionForm
from .models import Address
from .tasks import match_address_task


class SubscriptionFormView(FormView):
    template_name = 'subscription/subscription.html'
    form_class = SubscriptionForm
    success_url = '/success/'

    def form_valid(self, form):
        # address = Address(name=form.cleaned_data['name'],
        #                   address=form.cleaned_data['address'],
        #                   postalcode=form.cleaned_data['postalcode'],
        #                   city=form.cleaned_data['city'],
        #                   country=form.cleaned_data['country'],
        #                   email=form.cleaned_data['email'])
        task_message = {'name': form.cleaned_data['name'],
                          'address': form.cleaned_data['address'],
                          'postalcode': form.cleaned_data['postalcode'],
                          'city': form.cleaned_data['city'],
                          'country': form.cleaned_data['country'],
                          'email': form.cleaned_data['email']}
        # address.save()
        match_address_task.delay(task_message)
        self.request.session['name'] = form.cleaned_data['name']
        return super().form_valid(form)



class SuccessView(TemplateView):
    template_name = 'subscription/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.session.get('name', 'Subscriber')
        return context
