from django.db import models

class Department(models.Model):
    deptName = models.CharField(max_length=100, verbose_name="ชื่อแผนก")
    location = models.CharField(max_length=225, verbose_name="ตำแหน่ง")

    def __str__(self):
        return self.deptName

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อ-นามสกุล")
    age = models.IntegerField(verbose_name="อายุ")
    date = models.DateField(auto_now_add=True, verbose_name="วันที่เพิ่มข้อมูล")

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="แผนก"
    )

    def __str__(self):
        # ใช้ f-string เพื่อความสะดวกและป้องกัน Error กรณีค่าเป็น None
        return f"{self.name} (อายุ: {self.age})"

    class Meta:
        verbose_name = "พนักงาน"
        verbose_name_plural = "ข้อมูลพนักงาน"