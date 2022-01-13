import requests, json


response = requests.get(
    "http://127.0.0.1:8000/api/timogen/pdf",
    params={
        # 'therapist_name': 'Shanon Peché',
        # 'therapist_address': ['Avenue Louise 480', '1050 Ixelles'],
        # 'therapist_inami': '5-46533-62-527',
        # 'mutual_name': 'Union des Mutualités Libres',
        # 'mutual_address': ['Route de Lennik', 'PO Box 80500', '1070, Anderlecht'],
        # 'facture_ids': '200004/06 - 200004/07 - 200004/08',
        # 'patient_name': 'MBANE TE DJWA',
        # 'patient_niss': '36.11.11-353.53',
        # 'patient_address': 'Avenue Léopold Florent Lambin 5 Bte 17, 1160 Auderghem',
        # 'sessions': [],
        # 'total': '0',
        # 'therapist_bank_account': 'BANKACCOUNT',
        # 'therapist_bce': 'BCE',
    },
)

with open("result.pdf", "+wb") as f:
    f.write(response.content)
