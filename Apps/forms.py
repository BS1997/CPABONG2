from django import forms

# https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms
class SJlightForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(SJlightForm, self).__init__(*args, **kwargs)



    순자산 = forms.CharField()
    순이익_1 = forms.CharField()
    순이익_2 = forms.CharField()
    순이익_3 = forms.CharField()
    주식수 = forms.CharField()
    평가방법 = forms.ChoiceField(choices=(
                                        ('Option 1', '일반법인'),
                                        ('Option 2', '부동산과다법인'),
                                        ('Option 3', '순자산평가법인'),
                                        ))
    최대주주할증 = forms.ChoiceField(choices=(
                                        ('Option 1', '할증 없음'),
                                        ('Option 2', '10% 할증'),
                                        ('Option 3', '15% 할증'),
                                        ('Option 4', '25% 할증'),
                                        ('Option 5', '30% 할증'),
                                        ))