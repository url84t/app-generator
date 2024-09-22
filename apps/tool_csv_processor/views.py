from django.shortcuts import render
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .serializers import CSVUploadSerializer
import random
import string


def csv_processor(request):
    return render(request, "tools/csv-processor.html")  


def generate_random_string(length=5):
    """Generate a random string of fixed length."""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return "".join(random.choice(characters) for _ in range(length))


class CSVUploadView(APIView):
    def post(self, request, *args, **kwargs):
        # Validate and serialize the file input
        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():
            file = serializer.validated_data["file"]
            user_id = request.user.id  # Get the user ID

            # Create user-specific directory in media
            upload_path = os.path.join("user-{}/csv/".format(user_id))
            full_path = os.path.join(settings.MEDIA_ROOT, upload_path)

            # Ensure the directory exists
            if not os.path.exists(full_path):
                os.makedirs(full_path)

            # Generate a random 5-character string for the filename
            random_string = generate_random_string()

            # Get the file extension (e.g., '.csv')
            file_extension = os.path.splitext(file.name)[1]
            file_name = os.path.splitext(file.name)[0]

            # Create a new filename with the random string
            new_filename = f"{file_name}_{random_string}{file_extension}"

            # Define the full file path
            file_path = os.path.join(upload_path, new_filename)

            # Save the file
            file_name = default_storage.save(file_path, ContentFile(file.read()))

            # Return success response with file path
            return Response(
                {
                    "message": "CSV file uploaded successfully",
                    "file_path": os.path.join(settings.MEDIA_URL, file_name),
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)