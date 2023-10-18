from django.shortcuts import render
from adressbook import contacts

def contact_list(request):
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_detail(request, contact_id):
    contact = contact.object.get(pk=contact_id)
    return render(request, 'contacts/contact_detail.html', {'contact': contacts})