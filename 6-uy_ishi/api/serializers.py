from rest_framework import serializers
from .models import Genre, Book, Comment

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['genre'] # genre_id dan tashqari to'liq chiqsin

class GenreSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = '__all__'

    def get_books(self, obj):
        view = self.context.get('view')
        if view and view.action == 'retrieve':
            return BookDetailSerializer(obj.books.all(), many=True).data
        return [book.title for book in obj.books.all()]

class GenreRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField() # "courseni ham ma'lumoti to'liq chiqsin" degan shart uchun
    genre_id = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), source='genre', write_only=True)

    class Meta:
        model = Book
        exclude = ['description']
        extra_kwargs = {
            'price': {'required': True}
        }

    def get_course(self, obj):
        view = self.context.get('view')
        if view and view.action == 'retrieve':
            return GenreRelationSerializer(obj.genre).data
        return None

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at']
