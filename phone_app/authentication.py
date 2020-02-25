from django.contrib.auth.models import User

class EmailAuthBackend(object):
    def authenticate(self, username=None , password=None):
        print('zzzzzzzzzzDASSSSSSSSSSSSSSSSSSSSSSSSSSssssssssssssssssssssssssssssssssss')
        try:
            user = User.objects.get(email=username)
            print(user)
            print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            print('zzzzzzzzzzDASSSSSSSSSSSSSSSSSSSSSSSSSS')

            return None

    def get_user(self , user_id ):
        print('zzzzzzzzzzDASSSSSSSsaasasSSSSSSSSSSSSSSSSSSS')
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
