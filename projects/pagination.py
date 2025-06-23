from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 15 # Sets 15 items per page
    page_size_query_param = 'page_size' # Allows client to override page size with ?page_size=X
    max_page_size = 300 # Max page size a client can request