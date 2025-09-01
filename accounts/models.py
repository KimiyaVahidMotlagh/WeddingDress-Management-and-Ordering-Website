from django.contrib.auth.models import User
from django.db import models

class BodyMeasurement(models.Model):
    BODY_TYPE_CHOICES = [
        ('HOURGLASS', 'ساعت‌شنی'),
        ('RECTANGLE', 'مستطیل'),
        ('TRIANGLE', 'مثلث (گلابی)'),
        ('INVERTED_TRIANGLE', 'مثلث وارونه'),
        ('APPLE', 'گرد (سیب)'),
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="کاربر",
        related_name='bodymeasurement'
    )
    height = models.FloatField(
        verbose_name="قد (سانتی‌متر)",
        null=True,
        blank=True
    )
    bust = models.FloatField(
        verbose_name="دور سینه (سانتی‌متر)",
        null=True,
        blank=True
    )
    waist = models.FloatField(
        verbose_name="دور کمر (سانتی‌متر)",
        null=True,
        blank=True,
        help_text="مقدار باید بالای ناف و زیر دنده‌ها اندازه‌گیری شود"
    )
    high_hip = models.FloatField(
        verbose_name="دور بالای باسن (سانتی‌متر)",
        null=True,
        blank=True,
        help_text="حدود ۱۰ سانت زیر کمر"
    )
    hips = models.FloatField(
        verbose_name="دور باسن (سانتی‌متر)",
        null=True,
        blank=True
    )
    body_type = models.CharField(
        verbose_name="تیپ بدنی",
        max_length=20,
        choices=BODY_TYPE_CHOICES,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name="تاریخ ایجاد",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="آخرین بروزرسانی",
        auto_now=True
    )

    class Meta:
        verbose_name = "اندازه‌گیری بدن"
        verbose_name_plural = "اندازه‌گیری‌های بدن"
        ordering = ['-updated_at']

    def __str__(self):
        return f"اندازه‌گیری {self.user.username} - تیپ: {self.get_body_type_display()}"

    def calculate_body_type(self):
        """محاسبه خودکار تیپ بدنی براساس اندازه‌ها"""
        if not all([self.waist, self.hips, self.bust]):
            return None

        waist_hip_ratio = self.waist / self.hips
        bust_hip_ratio = self.bust / self.hips

        if waist_hip_ratio < 0.7 and 0.95 < bust_hip_ratio < 1.05:
            return 'HOURGLASS'
        elif waist_hip_ratio >= 0.85 and 0.95 < bust_hip_ratio < 1.05:
            return 'APPLE'
        elif 0.95 < bust_hip_ratio < 1.05:
            return 'RECTANGLE'
        elif bust_hip_ratio < 0.9:
            return 'TRIANGLE'
        elif bust_hip_ratio > 1.1:
            return 'INVERTED_TRIANGLE'
        else:
            if waist_hip_ratio < 0.75:
                return 'HOURGLASS'
            else:
                return 'RECTANGLE'

    def save(self, *args, **kwargs):
        """ذخیره خودکار تیپ بدنی هنگام ثبت"""
        if all([self.waist, self.hips, self.bust]):
            self.body_type = self.calculate_body_type()
        super().save(*args, **kwargs)