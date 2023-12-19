from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create users for development purposes'

    def handle(self, *args, **options):
        User = get_user_model()

        # Create member user
        member_user1 = User.objects.create_user(username='member_user1',
                                                user_type='MEMBER', 
                                                first_name="first_member1", 
                                                last_name="last_member1", 
                                                email="member_user1@email.com", 
                                                date_of_birth="2004-01-01",
                                                )
        member_user1 = User.objects.create_user(username='member_user2',
                                                user_type='MEMBER',
                                                first_name="first_member2", 
                                                last_name="last_member2", 
                                                email="member_user2@email.com", 
                                                date_of_birth="2004-01-02",
                                                )

        # Create admin user
        admin_user1 = User.objects.create_user(username='admin_user',
                                               user_type='ADMIN',
                                               first_name="first_admin",
                                               last_name="last_admin", 
                                               email="admin_user@email.com", 
                                               date_of_birth="2004-01-03",
                                               password="pbp12345"
                                               )

        self.stdout.write(self.style.SUCCESS('Users created successfully.'))
