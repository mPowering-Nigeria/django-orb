from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class ORBResourceAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list

    def create_detail(self, object_list, bundle):
        if bundle.request.user.userprofile.api_access == False:
            raise Unauthorized("You do not have API write access")
        return bundle.obj.create_user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class ORBAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list

    def create_detail(self, object_list, bundle):
        if bundle.request.user.userprofile.api_access == False:
            raise Unauthorized("You do not have API write access")
        return bundle.obj.create_user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        if bundle.request.user.userprofile.api_access == False:
            raise Unauthorized("You do not have API write access")
        return bundle.obj.create_user == bundle.request.user


class ORBResourceTagAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list

    def create_detail(self, object_list, bundle):
        if bundle.request.user.userprofile.api_access == False:
            raise Unauthorized("You do not have API write access")
        return bundle.obj.create_user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        if bundle.request.user.userprofile.api_access == False:
            raise Unauthorized("You do not have API write access")
        return True
