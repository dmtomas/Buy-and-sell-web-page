from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Order, OrderLine
from inicio.cart import Cart
from inicio.models import Product

def process_order(request):
  resp = "True"
  order = Order.objects.create(completed=True)
  cart = Cart(request)
  order_lines = list()
  for key, value in cart.cart.items():
    if value["quantity"] > Product.objects.get(id=key).amount:
      resp = "False"
  if resp == "True":
    for key, value in cart.cart.items():
      if value["quantity"] <= Product.objects.get(id=key).amount:
        Product.objects.filter(id = key).update(amount = Product.objects.get(id=key).amount - value["quantity"])
  else:
    print("feo no hay tantos productos")
    #order_lines.append(
     # OrderLine(product_id=key,
     # quantity=value["quantity"],
    #  order=order
  #    )
  #  )

 # OrderLine.objects.bulk_create(order_lines)
  
 # send_order_email(
  #  order=order,
 #   order_lines=order_lines,
 #   user_email= 'tomycrosta@gmail.com'
 # )

 # messages.success(request, "el pedido se ha creado correctamente")
  return redirect("carrito")



def send_order_email(**kwargs):
  subject = "Gracias por tu pedido"
  html_message = render_to_string("emails/nuevo_pedido.html", {
    "order": kwargs.get("order"),
    "order_lines": kwargs.get("order_lines")
  })

  plain_message = strip_tags(html_message)
  from_email = "tomy_crosta@hotmail.com"
  to = kwargs.get("user_email")
  send_mail(subject, plain_message, from_email, [to], html_message=html_message)
