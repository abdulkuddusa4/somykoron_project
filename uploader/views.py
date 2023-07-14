from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

from worker.my_worker import set_task


def upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uf = UploadedFile(word_size=form.cleaned_data.get('word_size'), file=request.FILES.get('file'))
            uf.save()
            file_id = uf.id

            with uf.file.open(mode='r') as file:
                # print([line for line in file])
                content = ' '.join(file.readlines())
                content.replace('\n', ' ')
                set_task(str(file_id), content, uf.word_size)
            return redirect('waiting_view', file_id=file_id)
    context = {
        'form': FileUploadForm(),
    }
    # return redirect('waiting_view',file_id=3)
    return render(request, 'uploader/index.html', context)
