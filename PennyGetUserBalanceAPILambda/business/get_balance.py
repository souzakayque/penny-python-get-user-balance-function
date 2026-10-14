from datetime import datetime
from pennyutils.domain.handlers.transactions_handler import get_monthly_summary
from pennyutils.core.dtos.transaction_dto import MonthlySummaryDTO

def run(aws_payload):
    print(f'{datetime.now()} Starting AWS lambda function')
    print(f'{datetime.now()} Body event: {aws_payload}')
    try:
        parameters = aws_payload.get("queryStringParameters") or {}
        id_user = int(parameters['id_user'])
        # month and year are optional: when both are missing the current month is used
        month = parameters.get('month') or None
        year = parameters.get('year') or None

        payload = MonthlySummaryDTO(id_user=id_user, month=month, year=year)

        response = get_monthly_summary(payload)

        print(f'Request OK: Response {response}')
        return response
    except ValueError as e:
        # invalid month/year: keep the validation message readable for the frontend
        print(f'Request Failed: Response {e}')
        raise
    except Exception as e:
        print(f'Request Failed: Response {e}')
        raise ValueError(f"Ocorreu um erro inesperado: {e}")
