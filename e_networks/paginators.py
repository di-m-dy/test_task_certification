from rest_framework.pagination import PageNumberPagination


class NetworkNodePagination(PageNumberPagination):
    """
    Кастомный пагинатор для узлов сети
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
