#-------------------------------------------------------------------------------
# @Author      :   Weihao Li
# @Time        :   2024/07/28 21:17:53
#-------------------------------------------------------------------------------
from flask import Blueprint


app_Analysis = Blueprint("analysis", __name__, template_folder="templates")

# import views
from Analysis import views