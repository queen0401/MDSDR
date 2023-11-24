#-------------------------------------------------------------------------------
# @Author      :   Weihao Li
# @Time        :   2023/11/19 13:14:46
#-------------------------------------------------------------------------------
from . import app_Index
from flask import render_template,request,session,redirect,url_for
import Forms

@app_Index.route("/", methods=['GET', 'POST'])
def Index():
	form = Forms.SearchForm()
	if request.method == 'POST' and form.validate():
		session['name'] = form.name.data
		return redirect(url_for('search.Search'))

	return render_template('Index.html',form = form)  