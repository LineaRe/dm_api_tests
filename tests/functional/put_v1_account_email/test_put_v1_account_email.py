from json import loads
from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi


def get_activation_token_by_login(login, response):
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])
        user_login = user_data['Login']

        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
    return token


def test_put_v1_account_login():

    # Регистрация пользователя

    account_api = AccountApi(host='http://5.63.153.31:5051')
    login_api = LoginApi(host='http://5.63.153.31:5051')
    mailhog_api = MailhogApi(host='http://5.63.153.31:5025')

    login = 'reyner_test21'
    email = f'{login}@mail.ru'
    password = '123456789'
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data=json_data)
    print(response.status_code)
    print(response.text)

    assert response.status_code == 201, f"Пользователь не был создан {response.json()}"


    # Получить письмо из почтового сервера

    response = mailhog_api.get_api_v2_messages(response)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Письмо не было получено"


    # Получить активационный токен

    token = get_activation_token_by_login(login, response)

    assert token is not None, f"Токен для пользователя {login} не был был получен"


    # Активация пользователя

    response = account_api.put_v1_account_token(token=token)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Пользователь не был активирован"


    # Авторизоваться

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Пользователь не смог авторизоваться"


    # Изменить емейл
    new_email = f'{login}_new@mail.ru'

    json_data = {
        'login': login,
        'email': new_email,
        'password': password
    }

    response = account_api.put_v1_account_email(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Не удалось изменить email"


    # Войти, получить 403

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 403, "Ожидалось 403 после смены email"


    # Найти токен для нового емейла для подтверждения смены

    new_response = mailhog_api.get_api_v2_messages(response)
    print(response.status_code)
    print(response.text)
    assert new_response.status_code == 200, "Письмо не было получено"

    new_token = get_activation_token_by_login(login, new_response)

    assert new_token is not None, f"Токен для пользователя {login} не был был получен"


    # Активация пользователя

    response = account_api.put_v1_account_token(token=new_token)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Пользователь не был активирован"

    # Логинимся успешно

    json_data = {
            'login': login,
            'password': password,
            'rememberMe': True,
        }

    response = login_api.post_v1_account_login(json_data=json_data)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Пользователь не смог авторизоваться"

