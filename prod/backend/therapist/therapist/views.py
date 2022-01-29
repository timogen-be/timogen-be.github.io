from rest_framework import generics, filters

from .models import Therapist
from .serializers import TherapistSerializer


class TherapistList(generics.ListAPIView):
    serializer_class = TherapistSerializer

    def _split_query(self, query):
        lst = []
        partial = ""
        query = query.translate({ord(e): "e" for e in "éèêë"})
        for letter in query + " ":
            if letter.isalpha():
                partial += letter
            else:
                lst.append(partial)
                partial = ""
        return lst

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Therapist.objects.all()
        uname = self.request.query_params.get("therapist")
        if not uname:
            return queryset
        uname_lst = self._split_query(uname)
        while uname_lst:
            queryset = queryset.filter(name__icontains=uname_lst.pop(0))
        return queryset


class TherapistDetail(generics.RetrieveAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer
