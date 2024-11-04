from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import time
import pandas as pd
from time import sleep

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'results'

# Asigură-te că directosdfareexistă
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/audit-tests')
def index():
    return render_template('home2.html')
@app.route('/review-tests')
def index2():
    return render_template('etva - Copy (2).html')
@app.route('/audittests')
def index3():
    return render_template('incarcare.html')
# @app.route('/run-tests', methods=['POST'])
# def upload_file():
#     if request.method=="POST":
#         client_name = "SAF-T"
        

#         selected_tests = request.files.getlist('saf-t-files')
#         # print(selected_tests, "-----selected_tests")
#         saved_files = []
#         # print(str(request.form))
#         # data = request.json
#         data = request.json
#         print(data, "dataaaaaaaaaaaaa")
#         # selected_tests = data.get('tests', [])
#         # selected_tests = data.get('tests', [])
#         print(selected_tests, "selected tests")
#         clients_checked = 'clients' in request.form
#         suppliers_checked = 'suppliers' in request.form
#         trial_balance_checked = 'trial_balance' in request.form
#         print(trial_balance_checked, "----trial balance checked")
#         general_ledger_checked = 'general_ledger' in request.form
#         sales_invoices_checked = 'sales_invoices' in request.form
#         purchase_invoices_checked = 'purchase_invoices' in request.form
#         payments_checked = 'payments' in request.form
#         tax_table_checked = 'tax_table' in request.form
#         print(f"Clients Checked: {clients_checked}")
#         print(f"Suppliers Checked: {suppliers_checked}")
#         print(f"Trial Balance Checked: {trial_balance_checked}")
#         print(f"General Ledger Checked: {general_ledger_checked}")
#         print(f"Sales Invoices Checked: {sales_invoices_checked}")
#         print(f"Purchase Invoices Checked: {purchase_invoices_checked}")
#         print(f"Payments Checked: {payments_checked}")
#         print(f"Tax Table Checked: {tax_table_checked}")
#         for file in selected_tests:
#             if file:
#                 file_path = os.path.join('D:/30. SAF-T Reversed/30. SAF-T Reversed/TEST', file.filename)
#                 file.save(file_path)
#                 saved_files.append(file.filename)
#                 accounts, customers, suppliers, invoices, invoices_sales, payments, je = parse_xml_to_dict(file_path)
#                 save_to_excel(
#                     accounts if trial_balance_checked else [],
#                     customers if clients_checked else [],
#                     suppliers if suppliers_checked else [],
#                     invoices if purchase_invoices_checked else [],
#                     invoices_sales if sales_invoices_checked else [],
#                     payments if payments_checked else [],
#                     je if general_ledger_checked else [],
#                     # je if general_ledger_checked else [],
#                     client_name,
#                     file_path.replace(".xml", ".xlsx")
#                 )
#         print(selected_tests, "=====================")
#         return send_from_directory('D:/30. SAF-T Reversed/30. SAF-T Reversed/TEST' , file.filename.replace(".xml", ".xlsx"))


if __name__ == '__main__':
    app.run(debug="True",host="0.0.0.0", port=3000)
