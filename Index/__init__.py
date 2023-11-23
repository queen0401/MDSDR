#-------------------------------------------------------------------------------
# @Author      :   Weihao Li
# @Time        :   2023/11/19 13:14:13
#-------------------------------------------------------------------------------
from flask import Blueprint

app_Index = Blueprint("index", __name__, template_folder="templates")

# import views
from Index import views