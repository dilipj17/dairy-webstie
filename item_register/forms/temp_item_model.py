from item_register.models import temp_Item_detail
from bootstrap_modal_forms.forms import BSModalForm

class TempItemForm(BSModalForm):
    class Meta:
        model = temp_Item_detail
        fields = ['item', 'quantity', 'price','is_buy']
