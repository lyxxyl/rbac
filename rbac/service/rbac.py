from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

import re
class ValidPermission(MiddlewareMixin):
    def process_request(self,request):
        current_path = request.path_info
        valid_url_list=["/login/","/reg/","/admin/.*"]
        for i in valid_url_list:
            ret1=re.match(i,current_path)
            if ret1:
                return None
        user_id = request.session.get("user_id",None)
        if  not user_id:
            return redirect('/login/')
        permission = request.session["permission"]
        flag = False
        for i in permission:
            i = "^%s$"%i
            ret = re.match(i, current_path)
            if ret:
                flag = True
                break
        if not flag:
            return HttpResponse("无权限")
