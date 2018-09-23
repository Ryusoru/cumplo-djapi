from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from . import models, forms

class QueryView(generic.CreateView):
    model = models.Query
    template_name = 'djapi/index.html'
    form_class = forms.QueryForm
    
    def get_success_url(self):
        return reverse('djapi:results', args=(self.object.id,))

def results(request, query_id):
    query = get_object_or_404(models.Query, pk=query_id)
    indicators = []
    
    indicators_list = models.FinantialIndicator.objects.all()
    for ind in indicators_list:
        if ind.query_set.filter(pk=query_id).exists():
            indicators.append(ind.indicator_name)
    
    return render(request, 'djapi/results.html', {'query': query, 'indicators': indicators})
