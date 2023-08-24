from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntryForm
from django.core.paginator import Paginator
from .models import Entry

def index(request):
    query = request.GET.get('q')
    entries = Entry.objects.all().order_by('surname')

    if query:
        entries = entries.filter(
            surname__icontains=query,
            name__icontains=query,
            organization__icontains=query
        )

    paginator = Paginator(entries, per_page=10)
    page_number = request.GET.get('page')
    page_entries = paginator.get_page(page_number)

    return render(request, 'phonebook/index.html', {'page_entries': page_entries, 'query': query})

def add_entry(request):
    if request.method == 'POST':
        Entry.objects.create(
            surname=request.POST['surname'],
            name=request.POST['name'],
            patronymic=request.POST['patronymic'],
            organization=request.POST['organization'],
            work_phone=request.POST['work_phone'],
            personal_phone=request.POST['personal_phone']
        )
        return redirect('index')
    return render(request, 'phonebook/add_entry.html')

def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'phonebook/edit_entry.html', {'form': form})

def detail_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'phonebook/detail_entry.html', {'entry': entry})

