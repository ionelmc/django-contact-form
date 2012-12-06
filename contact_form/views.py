
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, FormView

class ExtraContextMixin(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super(ExtraContextMixin, self).get_context_data(**kwargs)

class CompletedPage(ExtraContextMixin, TemplateView):
    template_name = "contact_form/contact_completed.html"

class ContactFormMixin(object):
    """
    Form view that sends email when form is valid. You'll need
    to define your own form_class and template_name.
    """
    def form_valid(self, form):
        form.send_email(self.request)
        return super(ContactFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse("contact_form:completed")

class ContactFormView(ContactFormMixin, ExtraContextMixin, FormView):
    pass

class ContactModelFormView(ContactFormMixin, ExtraContextMixin, CreateView):
    pass
