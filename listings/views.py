from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Listing
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def home(request):
    """
    Displays a random set of published listings on the homepage.
    """
    listings = Listing.objects.filter(is_published=True).order_by('?')[:6]  # Select 6 random listings
    context = {'listings': listings}
    return render(request, 'home.html', context)  # Assuming you have a template named home.html

@api_view(['GET'])
def search(request):
    """
    Searches and filters listings based on provided query parameters.
    """
    area = request.GET.get('area')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_bedrooms = request.GET.get('min_bedrooms')
    min_carpet_area = request.GET.get('min_carpet_area')
    sale_type = request.GET.get('sale_type')
    house_type = request.GET.get('house_type')

    # Build the queryset based on search parameters
    queryset = Listing.objects.filter(is_published=True)
    if area:
        queryset = queryset.filter(Q(location__icontains=area))
    if min_price:
        queryset = queryset.filter(price__gte=min_price)
    if max_price:
        queryset = queryset.filter(price__lte=max_price)
    if min_bedrooms:
        queryset = queryset.filter(bedrooms__gte=min_bedrooms)
    if min_carpet_area:
        queryset = queryset.filter(carpet_area__gte=min_carpet_area)
    if sale_type:
        queryset = queryset.filter(sale_type=sale_type)
    if house_type:
        queryset = queryset.filter(house_type=house_type)

    # Pagination (optional)
    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(queryset, request)
    serializer = ListingSerializer(page, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# Import the necessary serializer (replace with your actual serializer name)
from .serializers import ListingSerializer
