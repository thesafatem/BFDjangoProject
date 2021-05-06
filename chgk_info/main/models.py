from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser, User
from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


class Player(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class ChgkUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class ChgkUser(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    username = models.CharField(max_length=255)  # ошибка нарушения уникальности -> override, чтобы убрать unique=True
    profile = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True, related_name='chgk_user')

    objects = ChgkUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class TournamentBaseModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    number_of_questions = models.IntegerField()
    difficulty_level = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'

    def __str__(self):
        return self.name


class Synchronous(TournamentBaseModel):
    question_file = models.FileField(upload_to='media')

    class Meta:
        verbose_name = 'Синхрон'
        verbose_name_plural = 'Синхроны'


class Cup(TournamentBaseModel):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    posted_by = models.ForeignKey(ChgkUser, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Очник'
        verbose_name_plural = 'Очники'


class TournamentCompetitorsTeams(models.Model):
    tournament = models.ForeignKey(TournamentBaseModel, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=255, null=True)
    results = models.JSONField(default=None)

    class Meta:
        verbose_name = 'Команда-участница'
        verbose_name_plural = 'Команды-участницы'

    def __str__(self):
        return self.tournament.__str__() + ' ' + self.team.__str__()


class TournamentCompetitorsPlayers(models.Model):
    tournament_team = models.ForeignKey(TournamentCompetitorsTeams, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Игрок-участник'
        verbose_name_plural = 'Игроки-участники'

    def __str__(self):
        return self.tournament_team.__str__() + ' ' + self.player.__str__()


class Application(models.Model):
    synchron = models.ForeignKey(Synchronous, on_delete=models.CASCADE)
    representative = models.ForeignKey(ChgkUser, on_delete=models.SET_NULL, null=True, related_name='representative')
    host = models.ForeignKey(ChgkUser, on_delete=models.SET_NULL, null=True, related_name='host')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.synchron.__str__() + ' ' + self.representative.__str__() + ' ' + self.host.__str__()