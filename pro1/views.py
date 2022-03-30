
from .models import descr

from django.views.generic import ListView,DetailView


from .models import descr







class homeview(ListView):
    model=descr
    template_name="index.html"

    


