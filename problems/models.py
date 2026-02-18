from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Problem(models.Model):
    """Main model for workplace problems"""

    # Status choices
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('public', 'Public'),
    ]

    # Industry choices
    INDUSTRY_CHOICES = [
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('construction', 'Construction'),
        ('hospitality', 'Hospitality'),
        ('technology', 'Technology'),
        ('finance', 'Finance'),
        ('retail', 'Retail'),
        ('manufacturing', 'Manufacturing'),
        ('other', 'Other'),
    ]

    # Frequency choices
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('occasionally', 'Occasionally'),
    ]

    # Affected people choices
    AFFECTED_CHOICES = [
        ('just_me', 'Just me'),
        ('my_team', 'My team (5-20)'),
        ('my_company', 'My company (20+)'),
        ('my_industry', 'My industry (hundreds+)'),
    ]

    PAIN_LEVELS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    # Core fields
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    industry = models.CharField(
        max_length=50, choices=INDUSTRY_CHOICES, default='other')
    job_role = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='problems')
    featured_image = CloudinaryField('image', default='placeholder')
    # Problem details
    pain_level = models.IntegerField(
        choices=PAIN_LEVELS,
        default=1,
        help_text="Rate from 1 (minor annoyance) to 10 (critical issue)"
    )
    frequency = models.CharField(
        max_length=20, choices=FREQUENCY_CHOICES, default='daily')
    affected_people = models.CharField(
        max_length=20, choices=AFFECTED_CHOICES, default='just_me')
    workaround = models.TextField(blank=True, null=True)
    # Contact & engagement
    contact_info = models.EmailField(blank=True, null=True)
    show_contact = models.BooleanField(default=False)
    upvote_count = models.PositiveIntegerField(default=0)
    # Status & meta
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft')
    is_solved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"Title: {self.title}  - by - {self.author}"


class Take(models.Model):
    # Frequency choices
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('occasionally', 'Occasionally'),
    ]

    # Affected people choices
    AFFECTED_CHOICES = [
        ('just_me', 'Just me'),
        ('my_team', 'My team (5-20)'),
        ('my_company', 'My company (20+)'),
        ('my_industry', 'My industry (hundreds+)'),
    ]

    # Publication status
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('public', 'Public'),
    ]

    PAIN_LEVELS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    # Core fields
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name='takes')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='take_author')
    pain_level = models.IntegerField(
        choices=PAIN_LEVELS,
        default=1,
        help_text="Rate from 1 (minor annoyance) to 10 (critical issue)"
    )
    frequency = models.CharField(
        max_length=20, choices=FREQUENCY_CHOICES, default='daily')
    affected_people = models.CharField(
        max_length=20, choices=AFFECTED_CHOICES, default='just_me')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        title = str(self.problem.title)[:20]
        if len(title) >= 17:
            title = title[:17] + "..."
        return f"Take on: {title}  - by - {self.author}"
