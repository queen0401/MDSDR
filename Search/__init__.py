#-------------------------------------------------------------------------------
# @Author      :   Weihao Li
# @Time        :   2023/11/20 11:19:20
#-------------------------------------------------------------------------------
from flask import Blueprint


app_Search = Blueprint("search", __name__, template_folder="templates")

# import views
from Search import views