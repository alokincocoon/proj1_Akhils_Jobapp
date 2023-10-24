from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import JobApplicationModel
from . forms import JobApplicationForm
# creating views

"""
    View for the listing page.
    Displays a list of job applications in descending order of creation.
    Template: Listing.html
    Context variable: 'data' (list of job applications)
    """
class JobListView(ListView):
    model = JobApplicationModel
    template_name = 'Listing.html'
    context_object_name = 'data'
    ordering = ['-id'] #listing page ordering by LIFO principle

"""
    View for the new user page.

    Allows users to submit new job applications.
    Template: Newuser.html
    Form: JobApplicationForm
    Success URL: Redirects to the listing page upon successful form submission.
    """
class JobCreateView(CreateView):
    model = JobApplicationModel
    form_class = JobApplicationForm
    template_name = 'Newuser.html'
    success_url = reverse_lazy('listing')
    def form_valid(self,form):  #success message after the creation of a new user page
      messages.add_message(self.request,messages.INFO, 'Job application submitted successfully!')
      return super().form_valid(form)
    
"""
        Displays a success message after the creation of a new job application.

        Args:
        form (JobApplicationForm): The submitted form.

        Returns:
        super().form_valid(form): Calls the parent class method to handle form validation.
        """
class JobUpdateView(UpdateView):
    model = JobApplicationModel
    form_class = JobApplicationForm
    template_name = 'Edit.html'
    success_url = reverse_lazy('listing')
    def form_valid(self,form): #success message after the editing the page
      messages.add_message(self.request,messages.INFO, 'Job application edited successfully!')
      return super().form_valid(form)
    
"""
    View for the delete page.
    Allows users to delete existing job applications.
    Template: Delete.html (Requires a confirmation template)
    Success URL: Redirects to the listing page upon successful deletion.
"""
class JobDeleteView(DeleteView):
    model = JobApplicationModel
    template_name = 'Delete.html'  # Create a Delete.html template for confirmation
    success_url = reverse_lazy('listing')
