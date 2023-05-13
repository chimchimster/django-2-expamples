import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from io import BytesIO
import pdfkit


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':

        nonce = request.POST.get('payment_method_nonce', None)

        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True,
            }
        })

        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()

            path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

            subject = f'My shop invoice no. {order.id}'
            message = 'Please find attached the invoice for your recent purchase'
            email = EmailMessage(
                subject,
                message,
                ['admin@myshop.com'],
                [order.email],
            )

            html = render_to_string('orders/order/pdf.html', {'order': order})
            out = BytesIO()

            pdf = pdfkit.PDFKit(html, 'string', css=settings.STATIC_ROOT + 'css/pdf.css', configuration=config).to_pdf()

            email.attach(f'order_{order.id}.pdf',
                         pdf,
                         )
            email.send()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        client_token = braintree.ClientToken.generate()
        return render(request, 'payments/process.html', {'order': order, 'client_token': client_token})


def payment_done(request):
    return render(request, 'payments/done.html')


def payment_canceled(request):
    return render(request, 'payments/canceled.html')