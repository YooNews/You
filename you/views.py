from django.http import JsonResponse
from oauth2_provider.views.generic import ProtectedResourceView


class WhoAmI(ProtectedResourceView):

    def get(self, request, *args, **kwargs):
        return JsonResponse(
                {
                    'id': request.resource_owner.id,
                    'username': request.resource_owner.get_username(),
                }
            )
