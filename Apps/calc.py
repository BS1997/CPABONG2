from django.db import models

# Create your views here.

class sjlight_submission(models.Model):
    netasset      = models.IntegerField()
    netprofit1    = models.IntegerField()
    netprofit2    = models.IntegerField()
    netprofit3    = models.IntegerField()
    stocknum      = models.IntegerField()
    val_method    = models.CharField(max_length=20)
    val_bigholder = models.CharField(max_length=20)


def calculate_simple(request):
    dta = sjlight_submission()
    is_valid = True
    error_messages = []  # 에러 메시지를 저장할 리스트
    
    try:
        dta.netasset = request.POST['totalasset'].replace(',', '')
        순자산 = int(request.POST['totalasset'].replace(',', ''))
    except Exception as e:
        is_valid = False
        error_messages.append(f"순자산 입력 오류: {str(e)}")

    try:        
        dta.netprofit1 = request.POST['netprofit-1'].replace(',', '')
        순이익_1 = int(request.POST['netprofit-1'].replace(',', ''))
    except Exception as e:
        is_valid = False
        error_messages.append(f"순이익(1년차) 입력 오류: {str(e)}")

    try:
        dta.netprofit2 = request.POST['netprofit-2'].replace(',', '')
        순이익_2 = int(request.POST['netprofit-2'].replace(',', ''))
    except Exception as e:
        is_valid = False
        error_messages.append(f"순이익(2년차) 입력 오류: {str(e)}")

    try:
        dta.netprofit3 = request.POST['netprofit-3'].replace(',', '')
        순이익_3 = int(request.POST['netprofit-3'].replace(',', ''))
    except Exception as e:
        is_valid = False
        error_messages.append(f"순이익(3년차) 입력 오류: {str(e)}")

    try:
        dta.stocknum = request.POST['stocknum'].replace(',', '')
        주식수 = int(request.POST['stocknum'].replace(',', ''))
    except Exception as e:
        is_valid = False
        error_messages.append(f"주식수 입력 오류: {str(e)}")

    try:
        dta.val_method = request.POST['valuationtype']
        평가방법 = request.POST['valuationtype']
    except Exception as e:
        is_valid = False
        error_messages.append(f"평가방법 입력 오류: {str(e)}")

    try:
        dta.val_bigholder = request.POST['bigshareholder']
        최대주주입력 = request.POST['bigshareholder']
    except Exception as e:
        is_valid = False
        error_messages.append(f"최대주주 입력 오류: {str(e)}")
    
    if not is_valid:
        # 오류 메시지 반환
        return {"is_valid": False, "errors": error_messages}



    # dta.save()

    if is_valid == True:
        
        최대주주할증 = {'1':0,'2':0.1,'3':0.15,'4':0.2,'5':0.3}[최대주주입력]
        연금현가계수 = 3.79079
        순자산10per     = int(순자산 * 0.1)

        # 순자산가치 계산
        ##  영업권가치 계산
        가중평균순이익 = (순이익_1 * 3 + 순이익_2 * 2 + 순이익_3 * 1 ) / 6
        주당순이익_1 = int(순이익_1 / 주식수)
        주당순이익_2 = int(순이익_1 / 주식수)
        주당순이익_3 = int(순이익_1 / 주식수)
        영업권 = int(max((가중평균순이익 * 0.5 - 순자산10per) * 연금현가계수,0))
        주당영업권 = int(영업권 / 주식수)
        주당순자산 = int(순자산 / 주식수)
        영업권포함순자산 = 순자산 + 영업권
        # 주당영업권포함순자산 = 주당순자산 + 주당영업권
        주당영업권포함순자산 = int(영업권포함순자산 / 주식수)

        # 순손익가치 계산
        가중순이익1 = 순이익_1 * 3
        가중순이익2 = 순이익_2 * 2
        가중순이익3 = 순이익_3 * 1
        가중평균순이익 = int(( 가중순이익1 + 가중순이익2 + 가중순이익3 ) / 6)
        순손익가치 = 가중평균순이익 * 10
        주당순손익가치 = int(순손익가치 / 주식수)


        # 평가결과요약
        평가결과요약 = []
        평가결과요약.append(f'주당 순자산가치 : {주당영업권포함순자산:,}')
        평가결과요약.append(f'주당 순손익가치 : {주당순손익가치:,}')
        if 평가방법=='1':        
            주당평가액 = int((주당영업권포함순자산 * 2 + 주당순손익가치 * 3) / 5)        
            if 주당평가액 >= 주당영업권포함순자산*.8:
                평가결과요약.append(f'평가방법은 일반 - 순자산가치 가중치는 2, 순손익가치 가중치는 3 입니다.')
                최종평가방법 = '수익가치: 60% / 자산가치: 40%'
            else:
                평가결과요약.append(f'순자산가치와 순손익가치를 고려한 평가액보다 순자산평가액 X 80%가 더 크므로 순자산가치의 80%로 평가합니다')
                주당평가액 = int(주당영업권포함순자산 * .8)
                최종평가방법 = '순자산가치의 80%'

        elif 평가방법=='2':
            주당평가액 = int((주당영업권포함순자산 * 3 + 주당순손익가치 * 2) / 5)
            if 주당평가액 >= 주당영업권포함순자산*.8:
                평가결과요약.append(f'부동산 과다법인이므로 순자산가치 가중치는 3, 순손익가치 가중치는 2 입니다.')
                최종평가방법 = '수익가치: 40% / 자산가치: 60%'
            else:
                평가결과요약.append(f'순자산가치와 순손익가치를 고려한 평가액보다 순자산평가액 X 80%가 더 크므로 순자산가치의 80%로 평가합니다')
                주당평가액 = int(주당영업권포함순자산 * .8)
                최종평가방법 = '순자산가치의 80%'
        else:
            평가결과요약.append(f'순자산특정 평가법인으로 순자산가치로만 평가합니다.')
            주당평가액 = int((주당영업권포함순자산 * 5 + 주당순손익가치 * 0) / 5)
            최종평가방법 = '순자산가치의 100%'

        if 최대주주입력=='1':
            평가결과요약.append('1주당 최종평가금액 : {:,}'.format(주당평가액))
            평가결과요약.append('(회사의 전체 지분가치는 {:,})'.format(주당평가액 * 주식수))
        else:        
            평가결과요약.append('1주당 최종평가금액 : 최대주주할증 고려전 {:,}   /  최대주주할증{:.0%} 고려후 {:,}'.format(주당평가액,         최대주주할증, int(주당평가액*(1+최대주주할증))))
            평가결과요약.append('(회사전체지분가치  : 최대주주할증 고려전 {:,}   /  최대주주할증{:.0%} 고려후 {:,}'.format(주당평가액 * 주식수, 최대주주할증, int(주당평가액 * 주식수 * (1+최대주주할증))))


        할증고려후주당평가액 = int(주당평가액 * (1+최대주주할증))
        지분가치_할증고려전 = 주당평가액 * 주식수
        지분가치_할증고려후 = 할증고려후주당평가액 * 주식수


    try:    
        순자산 = str(순자산)
    except:
        pass

    try:    
        순이익_1 = str(순이익_1)
    except:
        pass
    
    try:    
        순이익_2 = str(순이익_2)
    except:
        pass
    
    try:    
        순이익_3 = str(순이익_3)
    except:
        pass
    
    try:    
        주식수    = str(주식수)
    except:
        pass
    
    return locals()