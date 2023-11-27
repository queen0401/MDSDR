#-------------------------------------------------------------------------------
# @Author      :   Weihao Li
# @Time        :   2023/11/20 11:19:58
#-------------------------------------------------------------------------------
from . import app_Search
import Forms
from flask import render_template,request,session
# from flask_pymongo import PyMongo
import pymongo

client = pymongo.MongoClient(host='127.0.0.1') #连接
db = client.mdsdap

def custom_max(value, arg):
    return max(value, arg)

def custom_min(value, arg):
    return min(value, arg)

from flask import redirect, url_for

@app_Search.route('/Searchpage', methods=['GET', 'POST'])
def Searchpage():
    session.pop('name',None)
    page = request.args.get('page', default=1, type=int)
    items_per_page = 10  # 每页显示的项数
    form = Forms.SearchForm()

    if request.method == 'POST' and form.validate():
        session['name'] = form.name.data
        return redirect(url_for('search.Search'))


    data = db.all_data.find()

    # 计算总页数
    total_pages = (data.count() - 1) // items_per_page + 1

    # 分页数据
    data = data.skip((page - 1) * items_per_page).limit(items_per_page)

    return render_template('Search.html', data=data, page=page, total_pages=total_pages, form=form, max=custom_max, min=custom_min)


@app_Search.route('/Search', methods=['GET', 'POST'])
def Search():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 10  # 每页显示的项数
    form = Forms.SearchForm()

    if request.method == 'POST' and form.validate():
        session['name'] = form.name.data
        return redirect(url_for('search.Search'))

    name = session.get('name', '')
    search_criteria = {
        '$or': [
            {'uniprot_id': name},
            {'chemical_name': name},
            {'label': name},
            {'icd11': name},
            {'source': name},
            {'variant': name},
            {'gene_symbol': name},
            {'disease_name': name},
            {'punchem_id': name}
        ]
    }

    # 如果是 GET 请求或表单验证失败，显示全部数据
    if name:
        data = db.all_data.find(search_criteria)
    else:
        data = db.all_data.find()

    # 计算总页数
    total_pages = (data.count() - 1) // items_per_page + 1

    # 分页数据
    data = data.skip((page - 1) * items_per_page).limit(items_per_page)

    return render_template('Search.html', name = name, data=data, page=page, total_pages=total_pages, form=form, max=custom_max, min=custom_min)