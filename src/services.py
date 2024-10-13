from src.models import Employee


def serialize_employee(employee: Employee) -> dict:
    return {
        'id': employee.id,
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'birth_date': employee.birth_date,
        'gender': employee.gender,
        'email': employee.email,
        'role': employee.role.title
    }


def serialize_employees(employees: list[Employee]) -> list[dict]:
    return list(
        serialize_employee(employee)
        for employee in employees
    )


def make_pika_url(pika_params: dict) -> str:
    protocol = pika_params.get('protocol')
    user = pika_params.get('user')
    password = pika_params.get('password')
    host = pika_params.get('host')
    port = pika_params.get('port')

    return f'{protocol}://{user}:{password}@{host}:{port}/'
