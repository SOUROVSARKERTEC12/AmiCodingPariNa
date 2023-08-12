from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import InputValue
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import InputValueSerializer
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'khoj/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'khoj/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'khoj/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


def khoj_search(request):
    if request.method == 'POST':
        input_values = [int(val) for val in request.POST['input_values'].split(',')]
        search_value = int(request.POST['search_value'])
        sorted_input = sorted(input_values, reverse=True)

        # Store sorted_input, user id, and timestamp in the database
        InputValue.objects.create(user=request.user, input_values=sorted_input)

        # Perform search and save the result
        result = search_value in input_values

        return render(request, 'khoj/search.html', {'result': result})

    return render(request, 'khoj/search.html')


class InputValueViewSet(viewsets.ViewSet):
    serializer_class = InputValueSerializer

    def list(self, request):
        user_id = self.request.query_params.get('user_id')

        if user_id:
            input_values = InputValue.objects.filter(user_id=user_id)
            serialized_data = InputValueSerializer(input_values, many=True).data

            response_data = {
                'status': 'success',
                'user_id': user_id,
                'payload': serialized_data
            }

            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'status': 'error', 'message': 'Missing user ID parameter.'}, status=status.HTTP_400_BAD_REQUEST)
