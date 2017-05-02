from django import forms
from django.forms.utils import ErrorList

# Don't allow the form to submit if the user is not logged in
class FormUserNeededMixin(object):
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
            return self.form_invalid(form)

class UserOwnerMixin(FormUserNeededMixin, object):
   def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["Use not allowed to change this data."])
            return self.form_invalid(form)