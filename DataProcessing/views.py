from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = os.path.join('media', uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Process the file with pandas
            df = pd.read_csv(file_path)
            first_five_rows = df.head().to_html()
            summary_stats = df.describe().to_html()
            missing_values = df.isna().sum().to_frame().to_html()

            # Generate histograms
            histograms = []
            for column in df.select_dtypes(include=['number']).columns:
                histogram = df[column].plot.hist().get_figure()
                histogram_path = os.path.join('static', f'{column}_histogram.png')
                histogram.savefig(histogram_path)
                histograms.append(f'{column}_histogram.png')
                histogram.close()
            
            return render(request, 'DataProcessing/analysis.html', {
                'first_five_rows': first_five_rows,
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'histograms': histograms
            })
    else:
        form = UploadFileForm()
    return render(request, 'DataProcessing/upload.html', {'form': form})
