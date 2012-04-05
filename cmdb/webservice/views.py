# Create your views here.
from django.shortcuts import render_to_response
from biz.SourceManager import QuerySourceManager

#query appbiz&appinstance through web and return the result on web
def queryInfoByIp2Web(request,ip):
    if 'ip' in request.GET and request.GET['ip']:
        rip = request.GET['ip']
    elif ip:
        rip = ip
    else:
        return
    
    appInstance = QuerySourceManager().getAppInstanceByIp(rip)
    appBizList = QuerySourceManager().getAppBizListByAppInstance(appInstance)    
    return render_to_response('query_result.html',{'appBiz':appBizList[0],'appInstance':appInstance})
    
#query appbiz&appinstance through http request and return the result to hessian
#def queryInfoByIp2Service(request,ip):
#    if ip:
#        appBizList = QuerySourceManager().queryAppBizByIp(ip)
#        appInstance = QuerySourceManager().queryAppInstanceByIp(ip)
#        
#    else:
#        return
    
    