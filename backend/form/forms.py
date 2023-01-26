from django import forms
from transactions.models import Transaction


class Form(forms.Form):
    code = forms.CharField(max_length=255)
    # class Meta:
    #     model = Transaction
    #     fields = [
    #         "type",
    #         "date",
    #         "value",
    #         "cpf",
    #         "card",
    #         "hour",
    #         "store_owner",
    #         "store_name",
    #     ]
    #     read_only_fields = [
    #         "type",
    #         "date",
    #         "value",
    #         "cpf",
    #         "card",
    #         "hour",
    #         "store_owner",
    #         "store_name",
    #     ]
