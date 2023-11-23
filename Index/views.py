#-------------------------------------------------------------------------------
# @Author      :   Weihao Li
# @Time        :   2023/11/19 13:14:46
#-------------------------------------------------------------------------------
from . import app_Index
from flask import render_template

@app_Index.route("/", methods=['GET', 'POST'])
def Index():
	return render_template('Index.html')  