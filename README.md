# فروشگاه اینترنتی Digikala Django

یک فروشگاه اینترنتی کامل، الهام‌گرفته از دیجی‌کالا که با فریم‌ورک Django توسعه داده شده است. این پروژه به‌صورت انفرادی و با تمرکز بر پیاده‌سازی منطق بک‌اند، مدیریت کاربران، سبد خرید، سفارش‌ها و آماده‌سازی برای محیط Production ساخته شده است.

## مشاهده آنلاین پروژه

🔗 [ورود به نسخه آنلاین فروشگاه](https://sydshop.liara.run/)

## امکانات پروژه

- نمایش فهرست و جزئیات محصولات
- دسته‌بندی محصولات
- جست‌وجوی محصولات
- نمایش قیمت، تخفیف و امتیاز محصولات
- سبد خرید مبتنی بر Session
- ثبت‌نام، ورود و خروج کاربران
- مدیریت اطلاعات و رمز عبور حساب کاربری
- ثبت و مدیریت آدرس‌های کاربران
- ثبت سفارش برای کاربران عضو و مهمان
- مشاهده تاریخچه و جزئیات سفارش‌ها
- نمایش تاریخ‌ها به‌صورت شمسی
- مدیریت محصولات، کاربران و سفارش‌ها از پنل مدیریت Django
- ذخیره‌سازی اطلاعات در PostgreSQL
- ذخیره فایل‌های رسانه‌ای در فضای ذخیره‌سازی S3
- مدیریت فایل‌های استاتیک با WhiteNoise
- استفاده از متغیرهای محیطی برای نگهداری اطلاعات حساس

## تصاویر پروژه

![نمای صفحه اصلی فروشگاه](images/home-page.jpg)

> نام و مسیر تصویر بالا را متناسب با نام عکس آپلودشده در مخزن تغییر دهید.

## فناوری‌های استفاده‌شده

- Python
- Django 5.2
- PostgreSQL
- Django ORM
- Django Templates
- HTML5
- CSS3
- Bootstrap
- JavaScript و AJAX
- Django Sessions
- django-jalali
- Gunicorn
- WhiteNoise
- S3-Compatible Object Storage
- Liara
- Git و GitHub

## اجرای پروژه روی سیستم شخصی

ابتدا مخزن را دریافت کنید:

```bash
git clone https://github.com/amirsayyadi/digikala-django.git
cd digikala-django
```

سپس محیط مجازی را بسازید:

```bash
python -m venv venv
```

محیط مجازی را در ویندوز فعال کنید:

```bash
venv\Scripts\activate
```

وابستگی‌های پروژه را نصب کنید:

```bash
pip install -r requirements.txt
```

فایل `.env.example` را به `.env` تبدیل کرده و متغیرهای موردنیاز را تنظیم کنید:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

در پایان دستورات زیر را اجرا کنید:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

اکنون پروژه از طریق آدرس زیر در دسترس است:

```text
http://127.0.0.1:8000/
```

## وضعیت پروژه

نسخه فعلی پروژه روی Liara دیپلوی شده و از پایگاه داده PostgreSQL و فضای ذخیره‌سازی ابری استفاده می‌کند.

فرایند ایجاد و ثبت سفارش در پروژه پیاده‌سازی شده است؛ بااین‌حال، در نسخه فعلی درگاه پرداخت بانکی به پروژه متصل نیست.

## توسعه‌دهنده

**Amirhosein Sayyadi**

Backend Developer — Python & Django

🔗 [GitHub Profile](https://github.com/amirsayyadi)
