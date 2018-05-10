from django.shortcuts import render
from django.http import HttpResponse
from .forms import NumberForm


def index(request):
    form = NumberForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("Number noted. Processing... ")
        else:
            print(form.errors)

    return render(request, 'tellifprime/get_number.html', {'form': form, })


def is_perfect_square(n):
    if n == 1:
        return True

    if n < 1:
        return False

    x = int(n ** 0.5)

    if x ** 2 == n:
        return True
    else:
        return False


def is_perfect_cube(n):
    if n == 1:
        return True

    if n < 1:
        return False

    x = int(round(n ** (1. / 3)))

    if x ** 3 == n:
        return True
    else:
        return False


def is_prime(n):
    if n == 2:
        return "It's Prime!"

    if n <= 0:
        return "Don't fool yourself"

    if n == 1:
        return "It's unity. " \
               "It's not a prime. " \
               "It's a perfect square"

    if n > 2:
        for i in range(2, int((n ** 0.5) + 1)):
            if n % i == 0:
                if is_perfect_square(n) and is_perfect_cube(n):
                    return "It's a perfect square of {} and a perfect cube of {}. ".format(int(n ** 0.5),
                                                                                           int(round(n ** (1. / 3))))
                if is_perfect_square(n):
                    return "Not a prime number. " \
                           "It is a perfect square of {}. \n ".format(int(n ** 0.5))

                if is_perfect_cube(n):
                    return "Not a prime number. " \
                           "It is a perfect cube of {}. \n ".format(int(round(n ** (1. / 3))))

                return "Not a Prime Number! "

    return "It's a Prime Number. Believe the machine."


def show_result(request):
    num = int(request.POST.get('number_value', 1))
    response = is_prime(num)
    return render(request, 'tellifprime/post_result.html', {'response': response, })
