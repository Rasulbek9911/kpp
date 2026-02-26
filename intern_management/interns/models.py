from django.db import models
from django.utils import timezone
from datetime import timedelta


class Intern(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='To\'liq ismi')
    passport_id = models.CharField(max_length=100, verbose_name='Pasport raqami', unique=True, null=True, blank=True)
    department = models.CharField(max_length=200, verbose_name='Bo\'lim', null=True, blank=True)
    reason = models.TextField(verbose_name='Sababi', null=True, blank=True)
    start_date = models.DateField(verbose_name='Boshlanish sanasi')
    end_date = models.DateField(verbose_name='Tugash sanasi')
    photo = models.ImageField(upload_to='interns/', verbose_name='Rasm', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='O\'zgartirilgan vaqti')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Amaliyotchi'
        verbose_name_plural = 'Amaliyotchilar'

    def __str__(self):
        return self.full_name

    @property
    def days_left(self):
        """Calculate remaining days"""
        if not self.end_date:
            return 0
        today = timezone.now().date()
        delta = self.end_date - today
        if delta.days < 0:
            return 0
        return delta.days

    @property
    def status(self):
        """Calculate status (Faol/Tugagan)"""
        if not self.end_date:
            return 'Kutilmoqda'
        today = timezone.now().date()
        if today <= self.end_date:
            return 'Faol'
        return 'Tugagan'

    @property
    def photo_preview(self):
        """Return photo for admin display"""
        if self.photo:
            return self.photo.url
        return None
