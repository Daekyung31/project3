from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib


def create_app():
    app = Flask(__name__)

    m_bank = joblib.load('model/model_bank.pkl')
    m_che = joblib.load('model/model_che.pkl')
    m_cir = joblib.load('model/model_cir.pkl')
    m_clo = joblib.load('model/model_clo.pkl')
    m_con = joblib.load('model/model_con.pkl')
    m_ele = joblib.load('model/model_ele.pkl')
    m_fin = joblib.load('model/model_fin.pkl')
    m_food = joblib.load('model/model_food.pkl')
    m_gas = joblib.load('model/model_gas.pkl')
    m_ins = joblib.load('model/model_ins.pkl')
    m_mac = joblib.load('model/model_mac.pkl')
    m_man = joblib.load('model/model_man.pkl')
    m_med = joblib.load('model/model_med.pkl')
    m_nonmetal = joblib.load('model/model_nonmetal.pkl')
    m_prec = joblib.load('model/model_prec.pkl')
    m_ser = joblib.load('model/model_ser.pkl')
    m_ste = joblib.load('model/model_ste.pkl')
    m_sto = joblib.load('model/model_sto.pkl')
    m_tel = joblib.load('model/model_tel.pkl')
    m_trans = joblib.load('model/model_trans.pkl')
    m_ware = joblib.load('model/model_ware.pkl')
    m_wood = joblib.load('model/model_wood.pkl')
    @app.route('/', methods = ['GET', 'POST']) # URL 끝에 /만 있는 기본 페이지를 정의
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':
            corona = int(request.form['corona'])
            corona_c = int(request.form['corona_c'])
            exch = float(request.form['exch'])
            exch_c = float(request.form['exch_c'])
            oil = float(request.form['oil'])
            oil_c = float(request.form['oil_c'])
            us = float(request.form['us'])
            us_c = float(request.form['us_c'])

        bank=0

        data = np.array([corona, corona_c, exch, exch_c, oil, oil_c, us, us_c]).reshape(1, -1)
        data = pd.DataFrame(data)
        
        bank = m_bank.predict(data)
        che = m_che.predict(data)
        cir = m_cir.predict(data)
        clo = m_clo.predict(data)
        con = m_con.predict(data)
        ele = m_ele.predict(data)
        fin = m_fin.predict(data)
        food = m_food.predict(data)
        gas = m_gas.predict(data)
        ins = m_ins.predict(data)
        mac = m_mac.predict(data)
        man = m_man.predict(data)
        med = m_med.predict(data)
        nonmetal = m_nonmetal.predict(data)
        prec = m_prec.predict(data)
        ser = m_ser.predict(data)
        ste = m_ste.predict(data)
        sto = m_sto.predict(data)
        tel = m_tel.predict(data)
        trans = m_trans.predict(data)
        ware = m_ware.predict(data)
        wood = m_wood.predict(data)

        # return render_template('index.html', bank = bank)

        return render_template('index.html',che = che,cir = cir,clo = clo,con = con,ele = ele,fin = fin,food = food,gas = gas,ins = ins,mac = mac,
        man = man,med = med,nonmetal = nonmetal,prec = prec,ser = ser,ste = ste,sto = sto,tel = tel,trans = trans,ware = ware,wood = wood, bank=bank)    

    # @app. route('/result', methods = ['GET', 'POST'])
    # def result():
    #     if request.method == 'POST':
    #         corona = float(request.form['corona'])
    #         corona_c = float(request.form['corona_c'])
    #         exch = float(request.form['exch'])
    #         exch_c = float(request.form['exch_c'])
    #         oil = float(request.form['oil'])
    #         oil_c = float(request.form['oil_c'])
    #         us = float(request.form['us'])
    #         us_c = float(request.form['us_c'])

    #     data = np.array([corona, corona_c, exch, exch_c, oil, oil_c, us, us_c]).reshape(1, -1)
    #     data = pd.DataFrame(data)
        
    #     bank = m_bank.predict(data)
    #     che = m_che.predict(data)
    #     cir = m_cir.predict(data)
    #     clo = m_clo.predict(data)
    #     con = m_con.predict(data)
    #     ele = m_ele.predict(data)
    #     fin = m_fin.predict(data)
    #     food = m_food.predict(data)
    #     gas = m_gas.predict(data)
    #     ins = m_ins.predict(data)
    #     mac = m_mac.predict(data)
    #     man = m_man.predict(data)
    #     med = m_med.predict(data)
    #     nonmetal = m_nonmetal.predict(data)
    #     prec = m_prec.predict(data)
    #     ser = m_ser.predict(data)
    #     ste = m_ste.predict(data)
    #     sto = m_sto.predict(data)
    #     tel = m_tel.predict(data)
    #     trans = m_trans.predict(data)
    #     ware = m_ware.predict(data)
    #     wood = m_wood.predict(data)


    #     return render_template('result.html', bank = bank,che = che,cir = cir,clo = clo,con = con,ele = ele,fin = fin,food = food,gas = gas,ins = ins,mac = mac,
    #     man = man,med = med,nonmetal = nonmetal,prec = prec,ser = ser,ste = ste,sto = sto,tel = tel,trans = trans,ware = ware,wood = wood)    

    return app
if __name__=='__main__':
    app = create_app()
    app.run(debug=True) 