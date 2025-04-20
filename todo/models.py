from django.db import models
# timezone.now() 함수는 장고 설정(settings.py)에서 지정한 시간대(timezone) 를 기준으로 반환해 줍니다.
from django.utils import timezone 


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # 기본 동작 보완: complete 값에 따라 completed_at을 자동으로 처리
    def save(self, *args, **kwargs):
        if self.complete and self.completed_at is None:
            self.completed_at = timezone.now()
        if not self.complete and self.completed_at is not None:
            self.completed_at = None
        super().save(*args, **kwargs)