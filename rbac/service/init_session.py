def set_session(request,user):
    request.session["user_id"] = user.pk
    permission_list = []
    ret = user.roles.all().values("permissions__url").distinct()
    for item in ret:
        permission_list.append(item['permissions__url'])
    request.session["permission"] = permission_list