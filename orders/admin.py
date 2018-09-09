from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import format_html
import csv
import datetime


def OrderDetail(obj):
    return format_html('<a href="{}">Переглянути</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))


def ExportToCSV(modeladmin, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
    ExportToCSV.short_description = 'Export CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', OrderDetail, 'size', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', ]
    list_filter = ['paid', 'created', 'updated']
    inLines = [OrderItemInline]
    actions = [ExportToCSV]


admin.site.register(Order, OrderAdmin)
