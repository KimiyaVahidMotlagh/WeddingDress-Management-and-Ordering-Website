from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Booking
from datetime import datetime, timedelta
import json
@login_required
def booking_page(request):
    """صفحه جدول رزرو (هفته جاری یا هفته‌های بعد)"""
    week_offset = int(request.GET.get("week", 0))
    start_date = datetime.today().date() + timedelta(weeks=week_offset)
    start_date = start_date - timedelta(days=start_date.weekday())  # شروع هفته (دوشنبه یا شنبه)

    days = []
    for i in range(7):
        day_date = start_date + timedelta(days=i)
        days.append({
            "name": day_date.strftime("%A"),  # مثلاً Monday
            "date_str": day_date.strftime("%Y-%m-%d"),
        })

    time_slots = [f"{h}:00" for h in range(10, 20)]  # از ۱۰ تا ۱۹

    # گرفتن رزروهای این هفته
    week_dates = [d["date_str"] for d in days]
    booked = Booking.objects.filter(date__in=week_dates)
    booked_slots = [f"{b.date}_{b.time_slot}" for b in booked]

    return render(request, "booking.html", {
        "days": days,
        "time_slots": time_slots,
        "booked_slots": booked_slots,
        "week_offset": week_offset,
        "show_header_footer": True,  # این خط را اضافه کنید
    })


@login_required
def create_booking(request):
    """ایجاد رزرو جدید (Ajax)"""
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            date = datetime.strptime(data["date"], "%Y-%m-%d").date()
            day_name = data["day_name"]
            time_slot = data["time_slot"]

            if Booking.objects.filter(date=date, time_slot=time_slot).exists():
                return JsonResponse({"success": False, "message": "این زمان قبلاً رزرو شده است."})

            booking = Booking.objects.create(
                user=request.user,
                date=date,
                day_name=day_name,
                time_slot=time_slot,
            )
            return JsonResponse({"success": True, "id": booking.id})

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request"})


@login_required
def my_bookings(request):
    """لیست رزروهای کاربر"""
    user_bookings = Booking.objects.filter(user=request.user).order_by("-date", "-time_slot")
    return render(request, "my-booking.html", {"user_bookings": user_bookings})
