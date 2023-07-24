import random
# Import Faker
from faker import Faker


from account.models import (
    Bank,
    Region,
    City,
    User,
    UserAccountManager,
    EmployeeSalary,
)
fake = Faker()

# Create regions and cities
Region.objects.bulk_create(
    [
        Region(region="Rabat-Sale"),
        Region(region="Grand Casablanca"),
        Region(region="Marrakech"),
    ]
)

City.objects.bulk_create(
    [
        City(city="Rabat", region_id=Region.objects.get(region="Rabat-Sale")),
        City(city="Sale", region_id=Region.objects.get(region="Rabat-Sale")),
        City(city="Casablanca", region_id=Region.objects.get(region="Grand Casablanca")),
        City(city="Marrakech", region_id=Region.objects.get(region="Marrakech")),
    ]
)

# Create banks
Bank.objects.bulk_create(
    [
        Bank(bank_name="Attijariwafa Bank"),
        Bank(bank_name="Banque Centrale Populaire"),
        Bank(bank_name="Banque Marocaine du Commerce Extérieur"),
        Bank(bank_name="Banque Nationale Agricole"),
        Bank(bank_name="Crédit du Maroc"),
    ]
)

# Create user manager
user_manager = UserAccountManager()

# Create users
for i in range(35):
    user = user_manager.create_user(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        password="password",
        bank_id=random.choice(Bank.objects.all()),
        city_id=random.choice(City.objects.all()),
    )
    EmployeeSalary.objects.create(user=user, salary=random.randint(5000, 10000))

# Create superuser
superuser = user_manager.create_superuser(
    email="admin@example.com",
    first_name="Admin",
    last_name="User",
    password="password",
    bank_id=random.choice(Bank.objects.all()),
    city_id=random.choice(City.objects.all()),
)
EmployeeSalary.objects.create(user=superuser, salary=random.randint(10000, 20000))


user_manager = UserAccountManager()
for i in range(3):
    User.create(
    email=fake.email(),
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    password='password',
    bank_id=random.choice(Bank.objects.all()),
    city_id=random.choice(City.objects.all()))
    
users = User.objects.all()
for user in users:
    salary = random.randint(10000, 20000)
    EmployeeSalary.objects.create(employee=user, salary=salary)
