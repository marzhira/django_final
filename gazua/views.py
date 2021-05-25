from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .predict_analysis import predict_stock

# Create your views here.

def first_view(request):
    return render(request, 'main/first_view.html', {})

def index(request):
    return render(request, 'main/index.html', {})

def analysis(request):
    return render(request, 'main/ml_analysis.html', {})

def resource(request):
    return render(request, 'main/resource.html', {})


def aboutus(request):
    return render(request, 'main/aboutus.html', {})


def predict_analysis(request):

    revenue = float(request.POST['revenue']) if request.POST['revenue'] != '' else 1965.20
    total_assets = float(request.POST['total_assets']) if request.POST['total_assets'] != '' else 0.26
    tangible_assets = float(request.POST['tangible_assets'])  if request.POST['tangible_assets']  != '' else 0.20
    current_assets = float(request.POST['current_assets']) if request.POST['current_assets'] != '' else 5.1
    inventories = float(request.POST['inventories'])  if request.POST['inventories']  != '' else 2.4
    growth_rate_of_revenue = float(request.POST['growth_rate_of_revenue'])  if request.POST['growth_rate_of_revenue']  != '' else 2.4
    current_ratio = float(request.POST['current_ratio'])  if request.POST['current_ratio']  != '' else 2.4
    print("***")
    quick_ratio = float(request.POST['quick_ratio'])  if request.POST['quick_ratio']  != '' else 2.4
    dept_ratio = float(request.POST['dept_ratio'])  if request.POST['dept_ratio']  != '' else 2.4
    capital_adequacy = float(request.POST['capital_adequacy'])  if request.POST['capital_adequacy']  != '' else 2.4
    operating_margin = float(request.POST['operating_margin'])  if request.POST['operating_margin']  != '' else 2.4
    return_on_equity = float(request.POST['return_on_equity'])  if request.POST['return_on_equity']  != '' else 2.4
    sales_per_person = float(request.POST['sales_per_person'])  if request.POST['sales_per_person']  != '' else 2.4
    fixed_asset_turnover = float(request.POST['fixed_asset_turnover'])  if request.POST['fixed_asset_turnover']  != '' else 2.4
    price_earnings_ratio = float(request.POST['price_earnings_ratio'])  if request.POST['price_earnings_ratio']  != '' else 2.4
    price_bookvalue_ratio = float(request.POST['price_bookvalue_ratio'])  if request.POST['price_bookvalue_ratio']  != '' else 2.4

    data_1d_array = [revenue, total_assets, tangible_assets, current_assets, inventories, growth_rate_of_revenue, current_ratio, quick_ratio, dept_ratio, capital_adequacy, operating_margin, return_on_equity, sales_per_person, fixed_asset_turnover, price_earnings_ratio, price_bookvalue_ratio]

    predict_result = predict_stock(data_1d_array)

    context = {'predict_result' : predict_result}
    return render(request, 'main/ml_analysis_result.html', context)
