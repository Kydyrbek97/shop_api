from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    full_link_server = f'http://34.81.142.249/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: \n{full_link}\n{full_link_server}',
        'kydyrbek.mamatkulov@gmail.com',
        [user],
        fail_silently=False
    )


def send_reset_email(user):
    code = user.activation_code
    email = user.email
    send_mail('Letter with password rest code!',
              f'Your reset code {code}', 'from@example.com',
              [email, ], fail_silently=False)


def send_notification(user_email, order_id, price):
    send_mail('Уведомления о создание заказа!',
              f''' Вы создали заказ №{order_id}, ожидайте звонка!
               Полная стоимость вашего заказа: {price}.
                Спасибо за то что выбрали нас!''',
              "from@example.com",
              [user_email, ],
              fail_silently=False
              )
