from django.db import models


# class CustomUserManager(BaseUserManager):
    # def _create_user(self, email, username, password, is_staff, is_superuser):
    #     now = timezone.now()

    #     if username != None:
    #         email = username

    #     if not email:
    #         raise ValueError("Email must be sent")
    #     email = self.normalize_email(email)
    #     user = self.model(email=email,
    #                       is_staff=is_staff,
    #                       is_active=True,
    #                       is_superuser=is_superuser,
    #                       last_login=now,
    #                       date_joined=now
    #                       )
    #     user.set_password(password)
    #     user.save(using=self.db)
    #     return user

    # def create_user(self, email=None, username=None, password=None, **extra_fields):
    #     return self._create_user(email, username, password, False, False, **extra_fields)

    # def create_superuser(self, email, username, password, **extra_fields):
    #     return self._create_user(email, username, password, True, True, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMIxin):
    # email = models.EmailField('email address', max_length=255, unique=True)
    # first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    # last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    # is_staff = models.BooleanField('staff status', default=False)
    # is_active = models.BooleanField('active', default=True)
    # date_joined = models.DateTimeField('date joined', auto_now_add=True)
    # objects = CustomUserManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # class Meta:
    #     verbose_name = 'user'
    #     verbose_name_plural = 'users'

    # def get_absolute_url(self):
    #     return "/users/%s/" % urlquote(self.email)

    # def get_full_name(self):
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     return self.first_name

    # def email_user(self, subject, message, from_email=None):
    #     send_mail(subject, message, from_email, [self.email])


class Film(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    episode_id = models.IntegerField(null=True, blank=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=20, null=True, blank=True)
    producer = models.TextField(null=True, blank=True)
    release_date = models.TextField(null=True, blank=True)
    characters_url = models.TextField(null=True, blank=True)
    planets_url = models.TextField(null=True, blank=True)
    starships_url = models.TextField(null=True, blank=True)
    vehicles_url = models.TextField(null=True, blank=True)
    species_url = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class People(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    height = models.TextField(null=True, blank=True)
    mass = models.TextField(null=True, blank=True)
    hair_color = models.CharField(max_length=20, null=True, blank=True)
    skin_color = models.CharField(max_length=20, null=True, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    birth_year = models.TextField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    homeworld = models.ManyToManyField('main.Planet', blank=True)
    films = models.ManyToManyField('main.Film', blank=True)
    species = models.ManyToManyField('main.Species', blank=True, related_name='the_species')
    vehicles = models.ManyToManyField('main.Vehicles', blank=True, related_name='the_vehicles')
    starships = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    rotation_period = models.TextField(null=True, blank=True)
    orbital_period = models.TextField(null=True, blank=True)
    diameter = models.TextField(null=True, blank=True)
    climate = models.CharField(max_length=100, null=True, blank=True)
    gravity = models.CharField(max_length=100, null=True, blank=True)
    terrain = models.CharField(max_length=100, null=True, blank=True)
    surface_water = models.TextField(null=True, blank=True)
    population = models.TextField(null=True, blank=True)
    residents = models.ManyToManyField('main.People', blank=True)
    films = models.ManyToManyField('main.Film', blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Starship(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    model = models.CharField(max_length=70, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    cost_in_credits = models.TextField(null=True, blank=True)
    length = models.TextField(null=True, blank=True)
    max_atmosphering_speed = models.TextField(null=True, blank=True)
    crew = models.TextField(null=True, blank=True)
    passengers = models.TextField(null=True, blank=True)
    cargo_capacity = models.TextField(null=True, blank=True)
    consumables = models.CharField(max_length=40, null=True, blank=True)
    hyperdrive_rating = models.TextField(null=True, blank=True)
    MGLT = models.TextField(null=True, blank=True)
    starship_class = models.CharField(max_length=100, null=True, blank=True)
    pilots = models.ManyToManyField('main.People', blank=True)
    films = models.ManyToManyField('main.Film', blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    classification = models.CharField(max_length=60, null=True, blank=True)
    designation = models.CharField(max_length=60, null=True, blank=True)
    average_height = models.IntegerField(null=True, blank=True)
    skin_colors = models.CharField(max_length=100, null=True, blank=True)
    hair_colors = models.CharField(max_length=100, null=True, blank=True)
    eye_colors = models.CharField(max_length=100, null=True, blank=True)
    average_lifespan = models.TextField(null=True, blank=True)
    homeworld = models.CharField(max_length=100, null=True, blank=True)
    language = models.TextField(max_length=100, null=True, blank=True)
    #people = models.ManyToManyField('main.People', blank=True)
    films = models.ManyToManyField('main.Film', blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Vehicles(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    model = models.CharField(max_length=150, null=True, blank=True)
    manufacturer = models.CharField(max_length=150, null=True, blank=True)
    cost_in_credits = models.IntegerField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    max_atmosphering_speed = models.IntegerField(null=True, blank=True)
    crew = models.IntegerField(null=True, blank=True)
    passengers = models.IntegerField(null=True, blank=True)
    cargo_capacity = models.IntegerField(null=True, blank=True)
    consumables = models.TextField(null=True, blank=True)
    vehicle_class = models.CharField(max_length=200, null=True, blank=True)
    pilots = models.CharField(max_length=200, null=True, blank=True)
    films = models.ManyToManyField('main.Film', blank=True)

    def __unicode__(self):
        return self.name

