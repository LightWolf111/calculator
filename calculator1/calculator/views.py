from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calculate(request):
    length = request.POST.get('length')
    width = request.POST.get('width')

    perimeter = None
    area = None
    error_message = None

    if length and width:
        try:
            length = float(length)
            width = float(width)
            if length <= 0 or width <= 0:
                error_message = "Введите положительные числа"
            else:
                perimeter = 2 * (length + width)
                area = length * width
        except ValueError:
            error_message = "Введите числовые значения"

    return render(request, 'home.html', {'length': length, 'width': width, 'perimeter': perimeter, 'area': area, 'error_message': error_message})

