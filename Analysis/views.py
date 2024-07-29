#-------------------------------------------------------------------------------
# @Author      :   Weihao Li
# @Time        :   2024/07/28 21:26:21
#-------------------------------------------------------------------------------
from . import app_Analysis
from flask import render_template,request,session,redirect, url_for, send_file
import Forms
import pymongo
import numpy


client = pymongo.MongoClient(host='127.0.0.1', username='mdsap_user', password='123456', authSource='mdsap')
db = client.mdsap

def count_data(str):
	pipeline = [
		{
			'$group': {
				'_id': '$'+ str,
				'count': {'$sum': 1}
			}
		},
		{
			'$project': {
				'source': '$_id',
				'count': 1,
				'_id': 0
			}
		}
	]
	
	result = list(db.all_data.aggregate(pipeline))
	# 分别获取数据源和对应的数量
	data_name = [entry['source'] for entry in result]
	counts = [entry['count'] for entry in result]
	return data_name, counts

def ddg_distributation():
	ddg_values = list(db.all_data.find({}, {"ddg": 1}))
	ddg_list = [item["ddg"] for item in ddg_values if "ddg" in item]
	ddg_list = [i for i in ddg_list if not numpy.isnan(i)]
	start_range = -10
	end_range = 10
	interval = 0.5

	# 计算区间数量
	num_intervals = int((end_range - start_range) / interval) + 1

	# 初始化区间统计字典
	interval_counts = {round(start_range + i * interval, 1): 0 for i in range(num_intervals)}

	# 将浮点数分配到相应的区间
	for number in ddg_list:
		for key in interval_counts:
			if key <= number < key + interval:
				interval_counts[key] += 1
				break

	# 将字典转换为两个列表
	interval_names, interval_entries = zip(*interval_counts.items())
	return interval_names,interval_entries

@app_Analysis.route("/Analysis", methods=['GET', 'POST'])
def Analysis():
	form = Forms.SearchForm()
	if request.method == 'POST' and form.validate():
		session['name'] = form.name.data
		return redirect(url_for('search.Search'))
	source_name,source_count = count_data('source')
	disease_name,disease_count = count_data('disease_name')
	label_name,label_count = count_data('label')
	ddg_interval_names,ddg_interval_entries = ddg_distributation()

	filtered_diseases = [disease for disease, count in zip(disease_name, disease_count) if count > 120 and isinstance(disease,str)]
	filtered_disease_counts = [count for disease, count in zip(disease_name, disease_count) if count > 120 and isinstance(disease,str)]
	sorted_data = sorted(zip(filtered_diseases, filtered_disease_counts), key=lambda x: x[1], reverse=True)
	sorted_disease_names, sorted_disease_counts = zip(*sorted_data)
	filtered_labels = [label for label, count in zip(label_name, label_count) if count > 100 and isinstance(label,str)]
	filtered_label_counts = [count for label, count in zip(label_name, label_count) if count > 100 and isinstance(label,str)]
	sorted_data = sorted(zip(filtered_labels, filtered_label_counts), key=lambda x: x[1], reverse=True)
	sorted_label_names, sorted_label_counts = zip(*sorted_data)
	# print(ddg_interval_names)

	return render_template('Analysis.html',form = form, source_name=source_name, source_count=source_count, disease_count=sorted_disease_counts, disease_name=sorted_disease_names, label_name=sorted_label_names, label_count=sorted_label_counts, ddg_interval_names=ddg_interval_names, ddg_interval_entries=ddg_interval_entries)  
