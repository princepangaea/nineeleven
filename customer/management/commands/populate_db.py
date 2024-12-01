import random
from django.core.management.base import BaseCommand
from django.db import transaction
from customer.models import Customer
from address.models import Address, WorkArea, ElectricProvider
from faker import Faker

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create work areas if they don't exist
        work_areas = []
        for i in range(1, 30):
            work_area, _ = WorkArea.objects.get_or_create(work_area_values=i)
            work_areas.append(work_area)

        # Create electric providers if they don't exist
        providers = []
        provider_names = ['Cleco', 'Swepco', 'Entergy']
        for name in provider_names:
            provider, _ = ElectricProvider.objects.get_or_create(providername=name)
            providers.append(provider)

        # Common street types
        street_types = ['St', 'Ave', 'Blvd', 'Dr', 'Ln', 'Rd', 'Way', 'Circle', 'Court', 'Place']
        
        # Create 100 customers with addresses
        with transaction.atomic():
            # Clear existing data
            Address.objects.all().delete()
            Customer.objects.all().delete()
            
            for _ in range(100):
                # Create customer
                customer = Customer.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    mailing_address=f"{fake.building_number()} {fake.street_name()}",
                    mailing_city=fake.city(),
                    mailing_state=random.choice([state[0] for state in Customer.STATE_CHOICES]),
                    mailing_zip=fake.zipcode()
                )

                # Create 5 addresses per customer
                for i in range(5):
                    street_name = f"{fake.street_name()} {random.choice(street_types)}"
                    
                    Address.objects.create(
                        housenum=random.randint(100, 9999),
                        aptnum=random.choice([None, 'A', 'B', 'C', '1', '2', '3']) if random.random() < 0.3 else None,
                        lot_num=str(random.randint(1, 100)) if random.random() < 0.3 else None,
                        street=street_name,
                        city=fake.city(),
                        state=random.choice([state[0] for state in Address.STATE_CHOICES]),
                        zip=fake.zipcode(),
                        customer=customer,
                        work_area_num=random.choice(work_areas),
                        distance=random.randint(1, 100),
                        origin=fake.street_name(),
                        lr=random.choice(['L', 'R']),
                        provider=random.choice(providers),
                        notes=fake.text(max_nb_chars=200) if random.random() < 0.3 else None
                    )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with 100 customers and 500 addresses'))
